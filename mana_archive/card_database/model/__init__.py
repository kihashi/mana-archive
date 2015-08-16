"""SQLAlchemy Models

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///cards.db')

Base = declarative_base()

from .magic_card import MagicCard, Ruling, Color
