"""
A SQLAlchemy class for Magic card nicknames

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Unicode, ForeignKey

class Nickname(Base):
    __tablename__ = "nickname"

    card_id = Column(Unicode, ForeignKey("MagicCard.name"))
    nickname = Column(Unicode, primary_key=True)

    def __repr__(self):
        return self.nickname
