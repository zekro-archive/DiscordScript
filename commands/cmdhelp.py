"""
COMMAND: HELP
List all commands or display help of 
a specific command. 
"""

import command

from util import logger


class Help(command.Command):
    
    @staticmethod
    def get_invoke():
        return 'HELP'

    @staticmethod
    def get_args():
        return { 'COMMAND': False }
    
    @staticmethod
    def get_help_description():
        return 'List all commands or display help of a specific command. '

    def execute(self, passed_args: list):
        out = None
        registered_cmds = self.cmd_parser.registered_commands
        if len(passed_args) < 1:
            out = 'Commands:\n' \
                + '\n'.join(['  - %s' % c for c in registered_cmds])
        else:
            arg = passed_args[0]
            if not arg in registered_cmds:
                logger.error('Command "' + arg + '" does not exist')
                return
            out = 'Info for command "' + arg + '":\n\n'
            out += registered_cmds[arg](self.cmd_parser).get_help()
        logger.info(out)
