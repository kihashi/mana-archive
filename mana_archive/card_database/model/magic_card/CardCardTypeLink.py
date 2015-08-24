"""
A SQLAlchemy association table for MagicCard and CardType.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode, Integer
from sqlalchemy.orm import relationship
from ..base import Base, Session

class CardCardTypeLink(Base):
    __tablename__ = "card_card_type_link"

    card_id = Column(Unicode, ForeignKey("MagicCard.name"), primary_key=True)
    card_type_id = Column(Unicode, ForeignKey("CardType.card_type"), primary_key=True)
    order = Column(Integer)
    card_type = relationship("CardType")

    def __repr__(self):
        return "Card: {CARD} | Type: {CARDTYPE}".format(CARD=self.card, CARDTYPE=self.card_type)
