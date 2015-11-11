"""MTG JSON Parser
A parser for MTGJSON extended data JSON files.
MTGJSON is located at http://mtgjson.com/

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)

Usage:
    mtgjson.py -h
    mtgjson.py [-s | --set] FILE

Options:
    -h --help      Show this message
    -s --set       Used to parse a single set file.
"""

import datetime
import json
from docopt import docopt
import traceback
from sqlalchemy.orm.exc import NoResultFound
from tqdm import tqdm
from unidecode import unidecode
from mana_archive.card_database import model
from mana_archive.card_database.db_init import formats

excluded_sets = [
    "Unglued",
    "Unhinged",
    "Vanguard"
]


def open_file(file_location):
    with open(file_location, 'r') as json_file:
        return json.load(json_file)


def _parse_file(file_json):
    for set_json in tqdm(file_json, leave=True, desc='MTG Sets', unit='Sets'):
        _parse_set(file_json[set_json])


def _parse_set(set_json):
    model.Base.metadata.create_all(model.base.engine)
    session = model.Session()
    if "name" in set_json and set_json['name'] not in excluded_sets:
        try:
            db_expansion = session.query(model.Expansion).filter_by(name=set_json['name']).one()
        except NoResultFound:
            db_expansion = model.Expansion(name=set_json['name'],
                                            abbreviation=set_json['code'])
            if 'oldCode' in set_json:
                db_expansion.old_code = set_json['oldCode']

            if 'gathererCode' in set_json:
                db_expansion.gatherer_code = set_json['gathererCode']

            if 'magicCardsInfoCode' in set_json:
                db_expansion.dot_info_code = set_json['magicCardsInfoCode']

            if 'onlineOnly' in set_json:
                db_expansion.online_only = True
            else:
                db_expansion.online_only = False

            db_expansion.release_date = datetime.datetime.strptime(set_json['releaseDate'], "%Y-%m-%d").date()
            db_expansion.border = set_json['border']
            db_expansion.type = set_json['type']
            if 'block' in set_json:
                db_expansion.block = set_json['block']
            session.add(db_expansion)
            session.commit()

        for card in tqdm(set_json['cards'], leave=True, desc=set_json['name'], unit='Cards'):
            try:
                _parse_card(card, db_expansion, session)
            except Exception as e:
                print("Error with " + card['name'])
                print(card)
                print(e)
                print(traceback.print_exc())
                exit()

def _parse_card(card_json, expansion, session):
    try:
        db_card = session.query(model.MagicCard).filter_by(name=card_json['name']).one()
    except NoResultFound:
        db_card = model.MagicCard()

        db_card.name = card_json['name']
        db_card.search_name = unidecode(card_json['name'].lower().replace("'", "").replace(",", ""))

        if 'cmc' in card_json:
            db_card.converted_mana_cost = card_json['cmc']

        if 'manaCost' in card_json:
            db_card.mana_cost = card_json['manaCost']

        if 'text' in card_json:
            # Since IRC doesn't support newlines, we replace them with pipes.
            db_card.rules_text = card_json['text'].replace("\n", " | ")

        if 'power' in card_json:
            db_card.power = card_json['power']

        if 'toughness' in card_json:
            db_card.toughness = card_json['toughness']

        if 'loyalty' in card_json:
            db_card.loyalty = card_json['loyalty']

        if 'layout' in card_json:
            try:
                db_layout = session.query(model.Layout).filter_by(layout=card_json['layout']).one()
            except NoResultFound:
                db_layout = model.Layout(layout=card_json['layout'])
                session.add(db_layout)
            db_card.layout = db_layout

        if 'names' in card_json:
            # Find the other card in the list of names
            alt_name = set(card_json['names']).difference([card_json['name']]).pop()
            db_alt_side = session.query(model.MagicCard).filter_by(name=alt_name).first()
            if db_alt_side is not None:
                db_card.alt_side = db_alt_side
                db_alt_side.alt_side = db_card

        if 'colors' in card_json:
            for card_color in card_json['colors']:
                try:
                    db_color = session.query(model.Color).filter_by(color=card_color).one()
                except NoResultFound:
                    db_color = model.Color(color=card_color)
                    session.add(db_color)
                link = model.CardColorLink()
                link.color = db_color
                db_card.colors.append(link)
                session.add(link)

        if 'supertypes' in card_json:
            for count, card_supertype in enumerate(card_json['supertypes']):
                try:
                    db_supertype = session.query(model.Supertype).filter_by(supertype=card_supertype).one()
                except NoResultFound:
                    db_supertype = model.Supertype(supertype=card_supertype)
                    session.add(db_supertype)
                link = model.CardSupertypeLink()
                link.order = count
                link.supertype = db_supertype
                db_card.supertypes.append(link)
                session.add(link)

        if 'types' in card_json:
            for count, card_type in enumerate(card_json['types']):
                try:
                    db_type = session.query(model.CardType).filter_by(card_type=card_type).one()
                except NoResultFound:
                    db_type = model.CardType(card_type=card_type)
                    session.add(db_type)
                link = model.CardCardTypeLink()
                link.order = count
                link.card_type = db_type
                db_card.card_types.append(link)
                session.add(link)

        if 'subtypes' in card_json:
            for count, card_subtype in enumerate(card_json['subtypes']):
                try:
                    db_subtype = session.query(model.Subtype).filter_by(subtype=card_subtype).one()
                except NoResultFound:
                    db_subtype = model.Subtype(subtype=card_subtype)
                    session.add(db_subtype)
                link = model.CardSubtypeLink()
                link.order = count
                link.subtype = db_subtype
                db_card.subtypes.append(link)
                session.add(link)

        if 'rulings' in card_json:
            for card_ruling in card_json['rulings']:
                db_ruling = model.Ruling(date=datetime.datetime.strptime(card_ruling['date'],
                              "%Y-%m-%d").date(),
                              text=card_ruling['text'])
                db_card.rulings.append(db_ruling)
                session.add(db_ruling)


        if 'legalities' in card_json:
            for format_pair in [x for x in card_json['legalities'] if card_json['legalities'] in formats]:
                db_legality = model.Legality(format=format_pair['format'], legality=format_pair['legality'])
                db_card.legalities.append(db_legality)
                session.add(db_legality)
    db_cardrelease = model.CardRelease()
    db_cardrelease.expansion = expansion
    db_cardrelease.card = db_card
    db_cardrelease.mtgoprice = model.Price(source="MTGO")
    db_cardrelease.tcgplayerprice = model.Price(source="TCGPlayer")

    if 'multiverseid' in card_json:
        db_cardrelease.multiverse_id = card_json['multiverseid']
    else:
        db_cardrelease.multiverse_id = 0

    if 'flavor' in card_json:
        db_cardrelease.flavor_text = card_json['flavor']

    if 'rarity' in card_json:
        db_rarity = session.query(model.Rarity).filter_by(rarity=card_json['rarity']).one()
        db_cardrelease.rarity = db_rarity

    if 'originalText' in card_json:
        if expansion.name == card_json['printings'][0]:
            db_card.printed_text = card_json['originalText'].replace("\n", " | ")

    session.commit()

def main(args):
    if args['--set']:
        print("Parsing set file {FILE}".format(FILE=args['FILE']))
        _parse_set(open_file(args['FILE']))
    else:
        print("Parsing card file {FILE}".format(FILE=args['FILE']))
        _parse_file(open_file(args['FILE']))


if __name__ == '__main__':
    args = docopt(__doc__)

    main(args)
