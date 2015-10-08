"""
A parser for MTGO pricing data

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from datetime import datetime
import traceback
import requests
from docopt import docopt
from tqdm import tqdm
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import or_
from mana_archive.card_database import model
from mana_archive import config

def get_file(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text.splitlines()

def parse_prices(prices):
    model.Base.create_all(model.base.engine)
    session = model.Session()
    for line in tqdm(prices):
        line_list = line.replace("<br>", "").strip().split("|")
        if line_list[0] != "BOOSTER":
            try:
                card_release = session.query(model.CardRelease).filter(model.CardRelease.card_id == line_list[3],
                                                                       or_(model.CardRelease.expansion.abbreviation == line_list[0],
                                                                           model.CardRelease.expansion.old_code == line_list[0],
                                                                           model.CardRelease.expansion.gatherer_code == line_list[0],
                                                                           model.CardRelease.expansion.mtgo_code == line_list[0],
                                                                           model.CardRelease.expansion.dot_info_code == line_list[0])
                                                                       ).one()
            except NoResultFound as e:
                print("Error with line\n" + line_list)
                print(e)
                print(traceback.print_exc())
                exit()
            else:
                if line_list[2] == "R":
                    card_release.mtgoprice.price = float(line_list[5])
                else:
                    card_release.mtgoprice.foil_price = float(line_list[5])
                card_release.mtgoprice.last_fetch = datetime.datetime.now()
                session.commit()

def main():
    parse_prices(get_file(config.mtgo_api_url))
