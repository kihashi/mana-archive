"""
A SQLAlchemy class for Magic card expansions

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, Integer, Date, Boolean
from ..base import Base, Session

class Expansion(Base):
    __tablename__ = "expansion"

    name = Column(Unicode, primary_key=True)
    abbreviation = Column(Unicode, index=True)
    old_code = Column(Unicode, index=True)
    gatherer_code = Column(Unicode, index=True)
    mtgo_code = Column(Unicode, index=True)
    dot_info_code = Column(Unicode, index=True)
    release_date = Column(Date)
    border = Column(Unicode)
    type = Column(Unicode)
    block = Column(Unicode)
    online_only = Column(Boolean)

    def __repr__(self):
        return self.abbreviation

