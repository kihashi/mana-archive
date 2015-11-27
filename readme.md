[ ![Codeship Status for kihashi/mana_archive](https://codeship.com/projects/27bebd90-6a56-0133-ccb1-62b058ef9788/status?branch=master)](https://codeship.com/projects/114842)

Mana Archive is a database and API for accessing information about cards from the Magic: The Gathering collectible card
game.

# Dependencies

* Python 3.4
* SQLAlchemy

# Data Sources

Mana Archive includes a parser for [MTGJSON][1]. Other data sources may be added in the future. If you would like
another data source, please open an issue and I will see about making a parser for it. Note that if the data source does
not include data, then that data will not be added to the database.

