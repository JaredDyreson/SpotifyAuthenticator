#!/usr/bin/env python3.8

import json
from datetime import datetime
import os

from SpotifyAuthenticator import application

class CredentialIngestor():
    def __init__(self, path: str):
        self.path = path
        self.map = self.get_map()
        self.user_id = self.get_user_id()
        self.credential_hash = self.get_credential_hash()
        self.expire_time = self.get_time_expires()

    def get_map(self) -> dict:
        with open(self.path, "r") as fp:
            return json.load(fp)

    def get_user_id(self) -> str:
        return self.map['user_id']

    def get_username(self) -> str:
        return self.map['username']

    def get_credential_hash(self) -> str:
        return self.map['oauth_token']

    def get_time_expires(self) -> datetime:
        return datetime.strptime(self.map['time_expires'], "%m/%d/%Y %H:%M:%S")

    def is_expired(self, time: datetime) -> bool:
        return self.expire_time < time
