[ ![Codeship Status for kihashi/mana_archive](https://codeship.com/projects/27bebd90-6a56-0133-ccb1-62b058ef9788/status?branch=master)](https://codeship.com/projects/114842)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/93d89cd6ec2b4e2f91197b35004ee0d8/badge.svg)](https://www.quantifiedcode.com/app/project/93d89cd6ec2b4e2f91197b35004ee0d8)
[![Stories in Ready](https://badge.waffle.io/kihashi/mana_archive.svg?label=ready&title=Ready)](http://waffle.io/kihashi/mana_archive)

Mana Archive is a database and API for accessing information about cards from the Magic: The Gathering collectible card
game.

# Dependencies

* Python 3.4
* SQLAlchemy

# Data Sources

Mana Archive includes a parser for [MTGJSON][1]. Other data sources may be added in the future. If you would like
another data source, please open an issue and I will see about making a parser for it. Note that if the data source does
not include data, then that data will not be added to the database.

[1]: http://mtgjson.com/
