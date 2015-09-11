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
from sqlalchemy.orm.exc import NoResultFound
from unidecode import unidecode
from mana_archive.card_database import model



def open_file(file_location):
    with open(file_location, 'r') as json_file:
        return json.load(json_file)


def _parse_file(file_json):
    for set_json in file_json:
        _parse_set(file_json[set_json])


def _parse_set(set_json):
    model.Base.metadata.create_all(model.base.engine)
    session = model.Session()
    if "name" in set_json:
        print("Now adding: {SETNAME}".format(SETNAME=set_json['name']))
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
            db_expansion.block = set_json['block']
            session.add(db_expansion)

    session.commit()


def main(args):
    if args['--set']:
        print("Parsing set file {FILE}".format(FILE=args['FILE']))
        _parse_set(open_file(args['FILE']))


if __name__ == '__main__':
    args = docopt(__doc__)

    main(args)
