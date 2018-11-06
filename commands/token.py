"""
COMMAND: TOKEN
Register Discord API token to authenticate
at the API.
"""

import command

class Token(command.Command):
    def get_invoke(self):
        return "TOKEN"

    def get_args(self):
        return ['apitoken_str']

    def execute(self, passed_args: list):
        print(passed_args)
        print(self.get_invoke())