"""
A SQLAlchemy class for Magic card supertypes.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode
from ..base import Base, Session

class Supertype(Base):
    __tablename__ = "supertype"

    supertype = Column(Unicode, primary_key=True)

    def __repr__(self):
        return self.supertype
