"""

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from paver.easy import *
import sys
sys.path.append( path.abspath(path('.')) )
from mana_archive.card_database import model
from mana_archive.card_database import db_init
from mana_archive.card_database.db_init.parsers.cards import mtgjson
from mana_archive.card_database.db_init.parsers.prices import mtgo


@task
def clean():
    path('cards.db').remove()


@task
def clean_all():
    clean()
    path('AllSets-x.json').remove()


@task
def download_data():
    if not path('AllSets-x,json').exists():
        sh('wget http://mtgjson.com/json/AllSets-x.json')


@task
def build():
    download_data()
    model.Base.metadata.create_all(model.base.engine)
    db_init.create_colors()
    db_init.create_layouts()
    db_init.create_rarities()
    mtgjson.main({'FILE': "AllSets-x.json", '--set': ''})
    mtgo.main({})

@task
def buildclean():
    clean_all()
    build()
