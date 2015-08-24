"""
A SQLAlchemy association table for MagicCard and Color.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, ForeignKey, Unicode
from sqlalchemy.orm import relationship

class CardColorLink(Base):
    __tablename__ = "card_color_link"

    card_id = Column(Unicode, ForeignKey("MagicCard.name"), primary_key=True)
    color_id = Column(Unicode, ForeignKey("Color.color"), primary_key=True)
    color = relationship("Color")

    def __repr__(self):
        return "Card: {CARD} | Color: {COLOR}".format(CARD=self.card, COLOR=self.color)
