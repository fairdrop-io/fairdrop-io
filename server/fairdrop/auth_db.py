import sqlite3
import uuid
import time
import datetime
from fairdrop.config import CONFIG
import urllib.request
from json import loads as json_loads


class Requests:
    create_tables = ("CREATE TABLE IF NOT EXISTS sessions(token TEXT PRIMARY KEY, address TEXT DEFAULT '', "
                     "authenticated BOOL DEFAULT 0, timestamp INTEGER DEFAULT 0)",
                     "CREATE TABLE IF NOT EXISTS users(address TEXT PRIMARY KEY, user BOOL DEFAULT 0, status TEXT DEFAULT '')",
                     "CREATE TABLE IF NOT EXISTS messages(address TEXT, timestamp INT, title TEXT, message TEXT DEFAULT '')")

    add_new_token = "REPLACE INTO sessions(token, timestamp) VALUES(?, ?)"
    link_address = "UPDATE sessions SET address=? WHERE token=?"
    get_address = "SELECT address FROM sessions WHERE token=?"
    set_auth = "UPDATE sessions SET authenticated=? WHERE token=?"
    is_token_auth = "select sum(authenticated) FROM sessions WHERE token=?"
    delete_old = "DELETE FROM sessions WHERE timestamp != -1 AND timestamp < ?"
    get_address_status = "SELECT status FROM users WHERE address=?"
    set_address_status = "REPLACE INTO users(address, user, status) VALUES(?, (SELECT user FROM users WHERE address=?), ?)"
    new_user = "REPLACE INTO users(address, user, status) VALUES(?, 1, (SELECT status FROM users WHERE address=?))"
    get_messages = "SELECT timestamp, title, message FROM messages WHERE address=? OR address='system' ORDER BY timestamp DESC"
    new_message = "INSERT INTO messages(address, timestamp, title, message) VALUES(?, ?, ?, ?)"
    get_addresses_like = "SELECT address FROM users WHERE user=1 AND status LIKE ?"


class AuthDb:
    def __init__(self):
        self.db = sqlite3.connect(CONFIG["db_path"], check_same_thread=False)
        cursor = self.db.cursor()
        for table in Requests.create_tables:
            cursor.execute(table)
        self.db.commit()
        self.delete_old()

    def get_address_status(self, address):
        cursor = self.db.cursor()
        cursor.execute(Requests.get_address_status, (address,))
        result = cursor.fetchall()
        if len(result) and len(result[0]):
            return result[0][0]
        return ""

    def new_token(self, token=None):
        if not token:
            token = uuid.uuid4().hex

        cursor = self.db.cursor()
        cursor.execute(Requests.add_new_token, (token, int(time.time()) + CONFIG["session_duration"] if CONFIG["session_duration"] != -1 else -1))
        self.db.commit()

        return token

    def link_address(self, token, address):
        cursor = self.db.cursor()
        cursor.execute(Requests.link_address, (address, token))
        self.db.commit()

        cursor = self.db.cursor()
        cursor.execute(Requests.new_user, (address, address))
        self.db.commit()

    def get_address(self, token):
        cursor = self.db.cursor()
        cursor.execute(Requests.get_address, (token, ))
        result = cursor.fetchall()
        if len(result) and len(result[0]):
            return result[0][0]
        return ""

    def auth(self, token, authenticated=True):
        cursor = self.db.cursor()
        cursor.execute(Requests.set_auth, (authenticated, token))
        self.db.commit()
        return authenticated
    
    def is_token_auth(self, token):
        cursor = self.db.cursor()
        cursor.execute(Requests.is_token_auth, (token,))
        result = cursor.fetchall()
        return result[0][0]
    
    def delete_old(self):
        cursor = self.db.cursor()
        cursor.execute(Requests.delete_old, (int(time.time()), ))
        self.db.commit()
        return True

    def new_message(self, address, title, message=""):
        cursor = self.db.cursor()
        cursor.execute(Requests.new_message, (address, int(time.time()), title, message))
        self.db.commit()
        return True

    def get_messages(self, address):
        cursor = self.db.cursor()
        cursor.execute(Requests.get_messages, (address,))
        result = cursor.fetchall()
        return result

    def get_addresses_like(self, status):
        cursor = self.db.cursor()
        cursor.execute(Requests.get_addresses_like, (status,))
        result = cursor.fetchall()
        return result
    
    def set_address_status(self, address, status=""):
        cursor = self.db.cursor()
        cursor.execute(Requests.set_address_status, (address, address, status))
        self.db.commit()
        return True
    
    def stop(self):
        self.db.close()


if __name__ == '__main__':
    print("I'm a module, I can't run!")
