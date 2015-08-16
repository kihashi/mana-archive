"""
A SQLAlchemy class for a Magic card type.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode

class CardType(Base):
    __table_name__ = "card_type"

    card_type = Column(Unicode, primary_key=True)

    def __repr__(self):
        return self.card_type
