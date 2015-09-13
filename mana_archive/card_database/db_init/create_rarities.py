"""
A function to add all MTG Rarities to the database.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from .. import model

def create_rarities():
    session = model.Session()
    for r in [("Common", "C"),
              ("Uncommon", "U"),
              ("Rare", "R"),
              ("Mythic Rare", "M"),
              ("Time Spiral: Special", "S"),
              ("Basic Land", "L")]:
        session.add(model.Rarity(rarity=r[0], abbreviation=r[1]))
    session.commit()
