"""
A SQLAlchemy Class for Magic card prices

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, Float, DateTime, Integer
from sqlalchemy.orm import relationship

class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    foil_price = Column(Float)
    link = Column(Unicode)
    last_fetch = Column(DateTime)
    source = Column(Unicode)

    def __repr__(self):
        return "[{EXP}]: {PRICE}".format(EXP=self.card_release.expansion.abbreviation, PRICE=str(self.price))
