"""
A SQLAlchemy Class for Magic Card Legalities

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, ForeignKey, Integer

class Legality(Base):
    __tablename__ = "legality"

    id = Column(Integer, primary_key=True)
    format = Column(Unicode)
    legality = Column(Unicode)
    card_id = Column(Unicode, ForeignKey("MagicCard.name"))

    def __repr__(self):
        return "{FORMAT}: {LEGALITY}".format(FORMAT=self.format, LEGALITY=self.legality)
