"""

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from paver.easy import task, path, sh
import sys
sys.path.append(path.abspath(path('.')))
from mana_archive.card_database import model
from mana_archive.card_database import db_init


@task
def clean():
    path('cards.db').remove()


@task
def clean_all():
    clean()
    path('AllSets-x.json').remove()


@task
def download_data():
    if not path('AllSets-x.json').exists():
        sh('wget http://mtgjson.com/json/AllSets-x.json')


@task
def build():
    download_data()
    model.Base.metadata.create_all(model.base.engine)
    db_init.create_colors()
    db_init.create_layouts()
    db_init.create_rarities()
    sh('python -m mana_archive.card_database.db_init.parsers.cards.mtgjson AllSets-x.json')
    sh('python -m mana_archive.card_database.db_init.parsers.prices.mtgo')

@task
def buildclean():
    clean_all()
    build()
