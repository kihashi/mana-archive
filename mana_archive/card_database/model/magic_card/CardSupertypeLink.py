"""
A SQLAlchemy association table for MagicCard and Supertype

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode, Integer

class CardSupertypeLink(Base):
    __tablename__ = "card_supertype_link"

    card = Column(Unicode, ForeignKey("MagicCard.name"), primary_key=True)
    supertype = Column(Unicode, ForeignKey("Supertype.supertype"), primary_key=True)
    order = Column(Integer)

    def __repr__(self):
        return "Card: {CARD} | Supertype: {Supertype}".format(CARD=self.card, SUPERTYPE=self.supertype)
