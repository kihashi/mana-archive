"""
A SQLAlchemy association table for MagicCard and Color.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode

class CardColorLink(Base):
    __tablename__ = "card_color_link"

    card = Column(Unicode, ForeignKey("MagicCard.name"), primary_key=True)
    color = Column(Unicode, ForeignKey("Color.color"), primary_key=True)

    def __repr__(self):
        return "Card: {CARD} | Color: {COLOR}".format(CARD=self.card, COLOR=self.color)
