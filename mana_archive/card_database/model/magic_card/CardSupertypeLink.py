"""
A SQLAlchemy association table for MagicCard and Supertype

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode, Integer
from sqlalchemy.orm import relationship
from ..base import Base, Session

class CardSupertypeLink(Base):
    __tablename__ = "card_supertype_link"

    card_id = Column(Unicode, ForeignKey("magic_card.name"), primary_key=True)
    supertype_id = Column(Unicode, ForeignKey("supertype.supertype"), primary_key=True)
    order = Column(Integer)
    supertype = relationship("Supertype")

    def __repr__(self):
        return "Card: {CARD} | Supertype: {Supertype}".format(CARD=self.card, SUPERTYPE=self.supertype)
