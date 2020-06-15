import json
from fairdrop.auth_db import AuthDb

db = AuthDb()

with open("data/identities.json") as f:
    identities = json.load(f)
    
for address, status in identities.items():
    db.set_address_status(address.lower(), status)