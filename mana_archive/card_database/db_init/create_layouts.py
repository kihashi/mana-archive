"""
A function to add all MTG card layouts to the database.

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from .. import model

def create_layouts():
    session = model.Session()
    for l in [(u"normal", u"nml"),
              (u"split", u"spl"),
              (u"flip", u"flp"),
              (u"double-faced", u"dbl"),
              (u"token", u"tkn")]:
        session.add(model.Layout(layout=l[0], abbreviation=l[1]))
    session.commit()
