[ ![Codeship Status for kihashi/mana_archive](https://codeship.com/projects/27bebd90-6a56-0133-ccb1-62b058ef9788/status?branch=master)](https://codeship.com/projects/114842)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/93d89cd6ec2b4e2f91197b35004ee0d8/badge.svg)](https://www.quantifiedcode.com/app/project/93d89cd6ec2b4e2f91197b35004ee0d8)
[![Stories in Ready](https://badge.waffle.io/kihashi/mana_archive.svg?label=ready&title=Ready)](http://waffle.io/kihashi/mana_archive)

Mana Archive is a database and API for accessing information about cards from the Magic: The Gathering collectible card
game.

# Data Sources

Mana Archive includes a parser for [MTGJSON][1]. Other data sources may be added in the future. If you would like
another data source, please open an issue and I will see about making a parser for it. Note that if the data source does
not include data, then that data will not be added to the database.

[1]: http://mtgjson.com/

# Setting Up and Building

First, clone the repository and install the requirements:

```sh
git clone https://github.com/kihashi/mana_archive.git ./mana_archive
cd mana_archive
pip install -r requirements.txt
```

Mana Archive includes a [pavement][2] file for easy building. This provides some commands to easily set up the database.

[2]: http://paver.github.io/paver/

```sh
paver build # Downloads necessary data files and parses them. This will take some time.
```

## Paver Commands

These commands are provided for convenience, however, you can run the commands from each task should you so desire. See
the `pavement.py` file.

* clean -- Removes the database file.
* clean_all -- Removes the database file and the JSON data file.
* download_data -- Downloads the JSON data file.
* build -- Downloads the JSON data file, sets up the database models, creates static data (colors, layouts, and
  rarities) and parses the JSON data file. Also parses price data if the required API keys/URLs are provided in the
  config.
* buildclean -- `clean_all` then `build`.
