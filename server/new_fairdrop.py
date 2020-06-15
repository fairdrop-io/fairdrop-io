from json import load as json_load, dump as json_dump
from fairdrop.auth_db import AuthDb
from random import shuffle
import base58
import random
db = AuthDb()

with open("drop_config.json") as f:
    config = json_load(f)

winners = {}
for draw in config["draws"]:
    addresses = db.get_addresses_like(draw["status"])
    shuffle(addresses)
    draw_winners = 0
    for address in addresses:
        address = address[0]
        if address in winners:
            continue
        
        reedem_code = base58.b58encode(bytearray(random.getrandbits(8) for _ in range(10))).decode('utf-8')
        winners[address] = [draw["name"], draw["price"], reedem_code]
        db.new_message(address, draw["title"], message=draw["message"].replace("[reedem_code]", reedem_code))
        
        draw_winners += 1
        if draw_winners >= draw["winners"]:
            break
        
with open("drops/{}.json".format(config["name"]), "w") as f:
    json_dump(winners, f)
    
"""

Drop config example {"name": "drop_name", "draws": [{"name": "draw1", "status": "human", "winners": 10, "price": 1, "title": "message title", "message": "You won 1, reedem code: [reedem_code]"}]}

"""