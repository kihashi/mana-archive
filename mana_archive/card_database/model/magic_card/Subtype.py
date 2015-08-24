"""
A SQLAlchemy class for Magic card subtypes

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode

class Subtype(Base):
    __tablename__ = "subtype"

    subtype = Column(Unicode, primary_key=True)

    def __repr__(self):
        return self.subtype
