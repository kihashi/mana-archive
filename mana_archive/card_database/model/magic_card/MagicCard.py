"""
SQLAlchemy Class for a Magic Card

Author:    John Cleaver <cleaver.john.k@gmail.com>
Copyright: 2015 John Cleaver
License:   BSD (See LICENSE file)
"""

from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from ..base import Base, Session
from mana_archive.card_database.model.magic_card.CardRelease import CardRelease

class MagicCard(Base):
    __tablename__= "magic_card"

    layout_id = Column(Integer, ForeignKey('layout.layout'))
    layout = relationship("Layout", backref="cards")
    name = Column(Unicode, primary_key=True)
    search_name = Column(Unicode)
    alt_side_id = Column(Unicode, ForeignKey("magic_card.name"))
    alt_side = relationship("MagicCard", uselist=False, remote_side=[name], post_update=True)
    mana_cost = Column(Unicode)
    converted_mana_cost = Column(Integer)
    colors = relationship("CardColorLink")
    supertypes = relationship("CardSupertypeLink")
    card_types = relationship("CardCardTypeLink")
    subtypes = relationship("CardSubtypeLink")
    rules_text = Column(UnicodeText)
    printed_text = Column(UnicodeText)
    power = Column(Unicode)
    toughness = Column(Unicode)
    loyalty = Column(Integer)
    releases = relationship("CardRelease", backref="card")
    rulings = relationship("Ruling")
    nicknames = relationship("Nickname")
    legalities = relationship("Legality")

    @property
    def card_text(self):
        card_string = self.name

        if self.mana_cost:
            card_string += " | " + self.mana_cost

        card_string += " |"

        for supers in self.supertypes:
            card_string += " " + supers.supertype.supertype

        for types in self.card_types:
            card_string += " " + types.card_type.card_type

        if self.subtypes:
            card_string += " --"
            for subs in self.subtypes:
                card_string += " " + subs.subtype.subtype

        if self.rules_text:
            card_string += " | " + self.rules_text

        if self.power and self.toughness:
            card_string += " | " + self.power + "/" + self.toughness

        if self.loyalty:
            card_string += " | " + self.loyalty

        if self.releases:
            card_string += " | "
            for release in self.releases:
                card_string += release.expansion.abbreviation.upper() + "-" + release.rarity.abbreviation.upper() + ", "
            card_string = card_string[:-2]

        if self.alt_side:
            card_string += " | " + "Alt: " + self.alt_side.name

        return card_string


    @property
    def printed_text_output(self):
        if self.printed_text is not None:
            return self.name + " | " + self.printed_text

    def ruling_text(self, ruling_number):
        if ruling_number >= len(self.rulings):
            ruling_number = len(self.rulings)
        elif ruling_number <= 0:
            ruling_number = 1
        return (self.rulings[ruling_number - 1], ruling_number, len(self.rulings))

    def flavor_text(self, set=None):
        if set is None:
            for release in self.releases:
                if release.flavor_text is not None:
                    return release.flavor_text
            else:
                return None
        else:
            session = Session()
            return session.query(CardRelease).filter_by(card_id=self.name, expansion=set).one()


    @property
    def legality_text(self):
        legality_text = self.name
        for l in self.legalities:
            legality_text += " | " + l.format + ": " + l.legality

        return legality_text

    @property
    def mtgoprice_text(self):
        output = self.name
        for release in self.releases:
            if release.mtgoprice.price is not None:
                output += " | " + release.mtgoprice
        if output == self.name:
            return None
        else:
            return output
