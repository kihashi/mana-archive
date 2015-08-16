"""
A SQLAlchemy class for Magic card colors.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, ForeignKey

class Color(Base):
    __table_name__ = "color"

    color = Column(Unicode, primary_key=True)
    abbreviation = Column(Unicode)

    def __repr__(self):
        return self.abbreviation
