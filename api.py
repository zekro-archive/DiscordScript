"""
Class for performing requests to Discord API.
"""

import json
import requests

from util import logger


API_ROOT = 'https://discordapp.com/api/v6/'

METHOD_FUNCS = {
    'GET':    requests.get,
    'POST':   requests.post,
    'DELETE': requests.delete,
    'PUT':    requests.put
}


class APIRequests:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.undefined = True if api_token == '' else False
        pass
    
    @staticmethod
    def check_status_code(response: requests.Response, soft: bool = False) -> bool:
        accepted_codes = [200, 201, 202, 204, 205, 206, 207, 304]
        status_code = response.status_code
        if not status_code in accepted_codes:
            if soft:
                return False
            else:
                raise Exception('Response status ' + str(status_code))
        return True

    def _request(self, path: str, method: str, payload: dict = None) -> requests.Response:
        if self.undefined:
            raise Exception('APIRequest instance is undefined')
            
        methodfn = METHOD_FUNCS[method]
        headers = {
            'User-Agent':    'DiscordScript Interpreter',
            'Authorization': 'Bot ' + self.api_token,
            'Accept':        'application/json'
        }
        return methodfn(API_ROOT + path, headers=headers, json=payload)

    def get_current_user(self) -> requests.Response:
        return self._request('users/@me', 'GET')

    def get_users_guilds(self) -> requests.Response:
        return self._request('users/@me/guilds', 'GET')

    def get_guild(self, identifier: str, by_name: bool = False) -> requests.Response:
        if by_name:
            response = self.get_users_guilds()
            self.check_status_code(response)
            data = response.json()
            try:
                guild = next(g for g in data if g['name'] == identifier)
            except Exception:
                raise Exception('No guild found with name "' + identifier + '"')
            return self.get_guild(guild['id'])
        return self._request('guilds/' + identifier, 'GET')

    def get_guilds_channels(self, id: str) -> requests.Response:
        return self._request('guilds/' + id + '/channels', 'GET')

    def get_channel(self, guild_id: str, identifier: str, by_name: bool = False) -> requests.Response:
        if by_name:
            response = self.get_guilds_channels(guild_id)
            self.check_status_code(response)
            data = response.json()
            try:
                chan = next(c for c in data if c['name'] == identifier)
            except Exception:
                raise Exception('No guild found with name "' + identifier + '"')
            return self.get_channel(guild_id, chan['id'])
        print(identifier)
        return self._request('channels/' + identifier, 'GET')