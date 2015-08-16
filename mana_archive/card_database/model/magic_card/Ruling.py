"""
A SQLAlchemy class for a Magic card ruling.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, ForeignKey, Date, UnicodeText, Integer

class Ruling(Base):
    __table_name__ = "ruling"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    text = Column(UnicodeText)
    card = Column(Unicode, ForeignKey('magic_card.name'))

    def __repr__(self):
        return "[{DATE}]: {TEXT}".format(DATE=self.date, TEXT=self.text)
