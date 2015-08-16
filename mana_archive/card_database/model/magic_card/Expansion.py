"""
A SQLAlchemy class for Magic card expansions

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, Integer, Date

class Expansion(Base):
    __tablename__ = "expansion"

    name = Column(Unicode, primary_key=True)
    abbreviation = Column(Unicode)
    old_code = Column(Unicode)
    gatherer_code = Column(Unicode)
    mtgo_code = Column(Unicode)
    dot_info_code = Column(Unicode)
    release_date = Column(Date)
    border = Column(Unicode)
    type = Column(Unicode)
    block = Column(Unicode)

    def __repr__(self):
        return self.abbreviation

