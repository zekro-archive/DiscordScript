"""
Class for performing requests to Discord API.
"""

import json
import requests


API_ROOT = 'https://discordapp.com/api/v6/'

METHOD_FUNCS = {
    'GET':    requests.get,
    'POST':   requests.post,
    'DELETE': requests.delete,
    'PUT':    requests.put
}

api_instance = None

class APIRequests:
    def __init__(self, api_token: str):
        self.api_token = api_token
        pass
    
    def _request(self, path: str, method: str, payload: dict = None) -> requests.Response:
        methodfn = METHOD_FUNCS[method]
        headers = {
            'User-Agent':    'DiscordScript Interpreter',
            'Authorization': 'Bot ' + self.api_token,
            'Accept':        'application/json'
        }
        return methodfn(API_ROOT + path, headers=headers, json=payload)

    def get_current_user(self):
        return self._request('users/@me', 'GET')