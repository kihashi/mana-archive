"""
A SQLAlchemy class for Magic Card releases.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import UnicodeText, Integer, Column, Unicode, ForeignKey
from sqlalchemy.orm import relationship, backref

class CardRelease(Base):
    __tablename__ = "card_release"

    card_id = Column(Unicode, ForeignKey("magic_card.name"), primary_key=True)
    multiverse_id = Column(Integer)
    flavor_text = Column(UnicodeText)
    expansion_id = Column(Unicode, ForeignKey("expansion.name"), primary_key=True)
    expansion = relationship("Expansion")
    rarity_id = Column(Unicode, ForeignKey("rarity.rarity"))
    rarity = relationship("Rarity")
    mtgoprice_id = Column(Integer, ForeignKey("price.id"))
    mtgoprice = relationship("Price", uselist=False, backref=backref("card_release", uselist=False))
    tcgplayerprice_id = Column(Integer, ForeignKey("price.id"))
    tcgplayerprice = relationship("Price", uselist=False, backref=backref("card_release", uselist=False))

    def __repr__(self):
        return self.card.name + " - " + self.expansion

    @property
    def printed_flavor_text(self):
        if self.flavor_text is None:
            return None
        else:
            return "[{EXPANSION}]: {TEXT}".format(EXPANSION=self.expansion.abbreviation, TEXT=self.flavor_text)
