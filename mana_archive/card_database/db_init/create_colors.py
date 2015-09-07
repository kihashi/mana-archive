"""
A function to add all MTG Colors to the database.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from .. import model


def create_colors():
    session = model.Session()
    for c in [(u"White", u"W"),
              (u"Blue", u"U"),
              (u"Black", u"B"),
              (u"Red", u"R"),
              (u"Green", u"G")]:
        session.add(model.Color(color=c[0], abbreviation=c[1]))
    session.commit()
