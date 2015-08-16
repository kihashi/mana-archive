"""
A SQlAlchemy class for Magic card layouts.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Unicode, Column
from sqlalchemy.orm import relationship

class Layout(Base):
    __tablename__ = "layout"

    layout = Column(Unicode)
    abbreviation = Column(Unicode)
    cards = relationship("MagicCard")

    def __repr__(self):
        return self.abbreviation

