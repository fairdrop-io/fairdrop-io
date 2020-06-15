from fairdrop.config import CONFIG
from fairdrop.auth_db import AuthDb
from json import loads as json_loads, dumps as json_dumps

from eth_keys.main import PublicKey, Signature
from Crypto.Hash import keccak
import rlp


def quote(s):
    s = s.replace("/", "%2F")
    s = s.replace(":", "%3A")
    return s


class Auth:
    def __init__(self):
        self.db = AuthDb()

    @staticmethod
    def get_nonce(token, address):
        return "signin-" + str(int(token.encode('utf-8').hex()) | int(address.encode('utf-8').hex()))

    def get_dna_url(self, token=None, get_token=False):
        token = self.db.new_token(token)
        url = "dna://signin/v1?token={}&callback_url={}&nonce_endpoint={}&authentication_endpoint={}"
        url = url.format(token, quote(CONFIG["callback_url"]), quote(CONFIG["nonce_endpoint"]), quote(CONFIG["authentication_endpoint"]))
        if CONFIG["favicon_url"]:
            url += "&favicon_url={}".format(quote(CONFIG["favicon_url"]))
        if get_token:
            return url, token
        else:
            return url

    def get_nonce_response(self, request, as_json=False):
        if type(request) == str:
            request = json_loads(request)
        self.db.link_address(request["token"], request["address"])
        response = {"success": True, "data": {}}
        response["data"]["nonce"] = self.get_nonce(request["token"], request["address"])
        if as_json:
            return response
        return json_dumps(response)

    def get_authentication_response(self, request, as_json=False):
        if type(request) == str:
            request = json_loads(request)
        response = {"success": True, "data": {}}
        response["data"]["authenticated"] = True
        address = self.db.get_address(request["token"])

        keccak_hash = keccak.new(digest_bits=256)
        #keccak_hash.update(rlp.encode(self.get_nonce(request["token"], address)))
        keccak_hash.update(self.get_nonce(request["token"], address).encode('utf-8'))
        nonce_hash = keccak_hash.digest()
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(nonce_hash)
        nonce_hash = keccak_hash.digest()

        new_address = PublicKey.recover_from_msg_hash(nonce_hash, Signature(bytes.fromhex(request["signature"][2:]))).to_address()

        response["data"]["authenticated"] = address == new_address
        self.db.auth(request["token"], authenticated=response["data"]["authenticated"])
        if as_json:
            return response
        return json_dumps(response)


auth = Auth()