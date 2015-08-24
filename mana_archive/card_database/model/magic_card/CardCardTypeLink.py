"""
A SQLAlchemy association table for MagicCard and CardType.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode, Integer

class CardCardTypeLink(Base):
    __tablename__ = "card_card_type_link"

    card = Column(Unicode, ForeignKey("MagicCard.name"), primary_key=True)
    card_type = Column(Unicode, ForeignKey("CardType.card_type"), primary_key=True)
    order = Column(Integer)

    def __repr__(self):
        return "Card: {CARD} | Type: {CARDTYPE}".format(CARD=self.card, CARDTYPE=self.card_type)
