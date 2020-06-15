# Sign in with Idena Python module

Written from scratch, this module adds sign in with idena functionality to Python apps and websites.

requirements: eth_keys

The module composed of auth.py that requires auth_db.py, the db backend.

Nonce and sessions as well as auth state are stored in a local sqlite Database.



Auth class within auth.py follows the "Sign in with Idena" protocol, with methods of the same name.  
Routes to access these methods are to be defined in a layer above (here, the webserver in "server" directory)


## Config

See config.py for the auth related config and endpoints.  


## Auth_db class

Auth_db also creates the "users" and "messages" tables that are used to store the main data iof the fairdrop service: messages for all users, that are then displayed on their profile page.  
Should you use auth_db in another context, you may need to remove fairdrop specific methods and add your own.

A more generic architecture will likely be proposed, with an independant pip module.
