"""
A function to add all MTG Colors to the database.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from .. import model


def create_colors():
    session = model.Session()
    for c in [("White", "W"),
              ("Blue", "U"),
              ("Black", "B"),
              ("Red", "R"),
              ("Green", "G")]:
        session.add(model.Color(color=c[0], abbreviation=c[1]))
    session.commit()
