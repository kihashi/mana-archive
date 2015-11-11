"""
A SQLAlchemy class for Magic Card releases.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import UnicodeText, Integer, Column, Unicode, ForeignKey
from sqlalchemy.orm import relationship, backref
from ..base import Base, Session

class CardRelease(Base):
    __tablename__ = "card_release"

    id = Column(Integer, primary_key=True)
    card_id = Column(Unicode, ForeignKey("magic_card.name"), index=True)
    multiverse_id = Column(Integer, index=True)
    flavor_text = Column(UnicodeText)
    expansion_id = Column(Unicode, ForeignKey("expansion.name"), index=True)
    expansion = relationship("Expansion")
    rarity_id = Column(Unicode, ForeignKey("rarity.rarity"))
    rarity = relationship("Rarity")
    mtgoprice_id = Column(Integer, ForeignKey("price.id"))
    mtgoprice = relationship("Price",
                             uselist=False,
                             foreign_keys="CardRelease.mtgoprice_id")
    tcgplayerprice_id = Column(Integer, ForeignKey("price.id"))
    tcgplayerprice = relationship("Price",
                                  uselist=False,
                                  foreign_keys="CardRelease.tcgplayerprice_id")

    def __repr__(self):
        return self.card.name + " - " + str(self.expansion)

    @property
    def printed_flavor_text(self):
        if self.flavor_text is None:
            return None
        else:
            return "[{EXPANSION}]: {TEXT}".format(EXPANSION=self.expansion.abbreviation, TEXT=self.flavor_text)
