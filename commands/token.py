"""
COMMAND: TOKEN
Register Discord API token to authenticate
at the API. Also, the token will be checked
after registration for validity.
"""

import command

from util import logger
from api import APIRequests

class Token(command.Command):
    
    @staticmethod
    def get_invoke():
        return 'TOKEN'

    @staticmethod
    def get_args():
        return { 'TOKEN': True }
    
    @staticmethod
    def get_help_description():
        return 'Set the Discord API Bot token to authenticate at the API with.'

    def execute(self, passed_args: list):
        self.cmd_parser.api_instance = APIRequests(passed_args[0])
        response = self.cmd_parser.api_instance.get_current_user()

        body = {}

        try:
            body = response.json()
        except:
            pass
        if response.status_code != 200:
            if response.status_code == 401:
                logger.fatal('RESPONSE 401 - UNAUTHORIZED - INVALID TOKEN')
            else:
                logger.fatal('RESPONSE ' + response.status_code + ': ', body)
            raise Exception('manual interruption')
        
        logger.info('Authorization successful')
        logger.debug('DATA: ', body)
