"""
A SQLAlchemy Class for Magic card rarity

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode

class Rarity(Base):
    __tablename__ = "rarity"

    rarity = Column(Unicode, primary_key=True)
    abbreviation = Column(Unicode)

    def __repr__(self):
        return self.rarity
