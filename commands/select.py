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
        # if len(passed_args) < 2:
        #     logger.fatal('MISSING 2. ARGUMENT: ID')
        #     raise Exception('manual interruption')

        api = self.cmd_parser.api_instance

        by_name = False
        if len(passed_args) > 2 and passed_args[1].upper() == 'BY' and passed_args[2].upper() == 'NAME':
            if len(passed_args) < 4:
                logger.fatal('MISSING ARGUMENT: [NAME]')
                raise Exception('manual interruption')
            by_name = True

        objecttype = passed_args[0].upper()
        identifier = passed_args[1] if len(passed_args) > 1 else None

        if by_name:
            identifier = passed_args[3]
        
        def __check_args_length(must: int, argname: str, soft: bool = False) -> bool:
            if len(passed_args) < must:
                if not soft:
                    logger.fatal('MISSING ARGUMENT: [%s]' % argname)
                    raise Exception('manual interruption')
                logger.error('MISSING ARGUMENT: [%s]' % argname)

        if objecttype == 'GUILD':
            __check_args_length(2, 'ID')
            response = api.get_guild(identifier, by_name)
            APIRequests.check_status_code(response)
            cache.selected = cache.Selection('GUILD', response.json())
        
        elif objecttype == 'GUILDS':
            response = api.get_users_guilds()
            api.check_status_code(response)
            cache.selected = cache.Selection('GUILDS', response.json())

        elif objecttype == 'CHANNEL':
            __check_args_length(2, 'ID')
            if by_name and (cache.selected == None or not cache.selected.type == 'GUILD'):
                logger.fatal('GUILD needs to be selected to select a channel by name')
                raise Exception('manual interruption')
            guild_id = cache.selected.data['id'] if cache.selected != None else '' 
            response = api.get_channel(guild_id, identifier, by_name)
            APIRequests.check_status_code(response)
            cache.selected = cache.Selection('CHANNEL', response.json())
            pass
        
        elif objecttype == 'USER':
            pass
        
        elif objecttype == 'ROLE':
            pass

        else:
            logger.error('UNSUPPORTED TYPE: ', objecttype)
            raise Exception('manual interruption')

        logger.debug('SELECTED:\n  - TYPE: ', cache.selected.type, '\n  - DATA: ', cache.selected.data)