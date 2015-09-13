"""

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from mana_archive.card_database import model
from mana_archive.card_database import db_init

model.Base.metadata.create_all(model.base.engine)
db_init.create_colors()
db_init.create_layouts()
db_init.create_rarities()
