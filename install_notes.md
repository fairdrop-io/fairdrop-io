# Install notes

Python3.5 min required

Required modules (see requirements.txt):  
sqlite3, tornado, eth_keys, pycryptodome

## config.txt

The main config file.  
Text file, key=value

Names should be self explicit.

## server.py

The main server. It will bind to port 8888 by default.  
Edit server.py and do `tornado_server.start(port=80)` to have it start on port 80 for instance.

We recommend not exposing the server directly to the internet, but configure apache or nginx as a reverse proxy frontend.  
This setup is out of scope for this doc.

The python server uses html templates from the "templates" dir to build its html output.  
Static content is directly served from the html/css and html/css directories, from the apache webserver above.

Run server.py from a `screen` so it can run in background.

## load_identities.py

This is to be run at every new epoch. This reads the identities states from data/identities.json and updates the local sql database.


## new_fairdrop.py

This is the script to run in order to trigger new drop. It reads the config data from drop_config.json (see mockup data in there), draws the winners and sends them the message with redeem code.  
Winners are also saved as json into the "drops" folder.


