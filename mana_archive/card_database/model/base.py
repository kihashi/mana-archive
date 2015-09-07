"""
Declares the SQLAlchemy Base object.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cards.db')

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)
