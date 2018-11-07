"""
COMMAND: SELECT
Select objects by id or name for further
command processes.
"""

import command

import cache
from util import logger
from api import APIRequests


class Select(command.Command):
    
    @staticmethod
    def get_invoke():
        return 'SELECT'

    @staticmethod
    def get_args():
        return { 
            'GUILD(S)|CHANNEL(S)|ROLE(S)|USER(S)': True,
            'BY NAME [ID|NAME]': False
        }
    
    @staticmethod
    def get_help_description():
        return 'Select an object by ID or NAME for further command operations.'

    def execute(self, passed_args: list):
        if len(passed_args) < 1:
            logger.fatal('MISSING 1. ARGUMENT: GUILD(S)|CHANNEL(S)|ROLE(S)|USER(S)')
            raise Exception('manual interruption')
        if len(passed_args) < 2:
            logger.fatal('MISSING 2. ARGUMENT: ID')
            raise Exception('manual interruption')

        by_name = False
        if passed_args[1].upper() == 'BY' and passed_args[2].upper() == 'NAME':
            if len(passed_args) < 5:
                logger.fatal('MISSING ARGUMENT: [NAME]')
                raise Exception('manual interruption')
            by_name = True

        if not by_name:
            arg = passed_args[0].upper()

            if arg == 'GUILD':
                if len(passed_args) < 2:
                    logger.fatal('MISSING ARGUMENT: [ID]')
                    raise Exception('manual interruption')
                response = self.cmd_parser.api_instance.get_guild(passed_args[1])
                APIRequests.check_status_code(response)
                cache.selected = cache.Selection('GUILD', response.json())
            elif arg == cache.Selection.TYPE.CHANNEL:
                pass

            elif arg == cache.Selection.TYPE.USER:
                pass

            elif arg == cache.Selection.TYPE.ROLE:
                pass
            else:
                logger.error('UNSUPPORTED TYPE: ', arg)
                raise Exception('manual interruption')

            logger.debug('SELECTED:\n  - TYPE: ', cache.selected.type, '\n  - DATA: ', cache.selected.data)