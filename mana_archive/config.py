"""
Loads the package configuration from file or env. variables.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

import configparser
import os

config = configparser.ConfigParser(os.environ)
config.read("config.ini")

mtgo_api_url = config.get('DEFAULT', 'mtgo_api_url', fallback=None)
tcgplayer_api_url = config.get('DEFAULT', 'tcgplayer_api_url', fallback=None)
tcgplayer_partner_code = config.get('DEFAULT', 'tcgplayer_partner_code', fallback=None)

test_db_url = config.get('DEFAULT', 'test_db_url', fallback=None)

