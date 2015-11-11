"""
A parser for MTGO pricing data

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)

Usage:
    mtgo.py
    mtgo.py FILE [--log=LOGLEVEL]
    mtgo.py -h

Options:
    -h --help       Show this message
    --log=LOGLEVEL  Specifies the logging level
"""

import logging
from datetime import datetime
import requests
from docopt import docopt
from tqdm import tqdm
from sqlalchemy.sql.expression import or_
from mana_archive.card_database import model
from mana_archive import config


excluded_sets = [
    "BOOSTER",
    "VAN",
    "PRM"
]


def get_file(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text.splitlines()

def parse_prices(prices):
    model.Base.metadata.create_all(model.base.engine)
    session = model.Session()
    for line in tqdm(prices, leave=True, desc='Cards', unit="Cards"):
        line = line.replace("<br>", "").strip().split("|")
        # Look for split cards
        if "/" in line[3]:
            card_names = line[3].split("/")
            line = [line, line]
            line[0][3] = card_names[0]
            line[1][3] = card_names[1]
        else:
            line = [line]
        for line_list in line:
            if line_list[0] not in excluded_sets:

                card_release = session.query(model.CardRelease)\
                               .filter(model.CardRelease.card_id == line_list[3]) \
                               .filter(
                                or_(
                                    model.CardRelease.expansion.has(abbreviation=line_list[0]),
                                    model.CardRelease.expansion.has(old_code=line_list[0]),
                                    model.CardRelease.expansion.has(gatherer_code=line_list[0]),
                                    model.CardRelease.expansion.has(mtgo_code=line_list[0]),
                                    model.CardRelease.expansion.has(dot_info_code=line_list[0])
                                )).first()
                if card_release is None:
                    logging.warning("Error with line:  %s", line_list)
                else:
                    if line_list[2] == "R":
                        card_release.mtgoprice.price = float(line_list[5])
                    else:
                        card_release.mtgoprice.foil_price = float(line_list[5])
                    card_release.mtgoprice.last_fetch = datetime.now()
                    session.commit()
            else:
                logging.info("Line from excluded set: %s", line_list)

def main(args):
    numeric_level = getattr(logging, args['--log'].upper(), None)
    logging.basicConfig(filename="mtgo.log", level=numeric_level)
    if args['FILE'] != "":
        logging.info("Loading prices from file: %s", args['FILE'])
        with open(args['FILE'], 'r', encoding="ISO-8859-1") as f:
            parse_prices(f)
    else:
        logging.info("Loading prices from URL: %s", config.mtgo_api_url)
        parse_prices(get_file(config.mtgo_api_url))


if __name__ == '__main__':
    args = docopt(__doc__)

    main(args)
