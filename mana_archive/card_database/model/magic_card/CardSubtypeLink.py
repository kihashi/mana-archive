"""
A SQLAlchemy association table for MagicCard and Subtype

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode, Integer
from sqlalchemy.orm import relationship
from ..base import Base, Session

class CardSubtypeLink(Base):
    __tablename__ = "card_subtype_link"

    card_id = Column(Unicode, ForeignKey("magic_card.name"), primary_key=True)
    subtype_id = Column(Unicode, ForeignKey("subtype.subtype"), primary_key=True)
    order = Column(Integer)
    subtype = relationship("Subtype")

    def __repr__(self):
        return "Card: {CARD} | Subtype: {SUBTYPE}".format(CARD=self.card, SUBTYPE=self.subtype)
