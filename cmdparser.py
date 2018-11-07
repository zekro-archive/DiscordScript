"""
Command parser which is used to parse raw commands
to execute functions in command classes and passing
argument data to them.
"""

import shlex

import command
from util import logger


class CommandParser:
    def __init__(self):
        self.registered_commands = dict()
        pass
    
    def _parse_command(self, command: str):
        cmd_split = shlex.split(command)
        invoke = cmd_split[0]
        args = cmd_split[1:]
        if invoke in self.registered_commands.keys():
            logger.debug('Trying executing command "%s"' % invoke)
            try:
                self.registered_commands[invoke]().execute(args)
            except Exception as e:
                logger.error('Failed executing command "' + invoke + '": ', e)
                exit(1)
        else:
            logger.error('Command "%s" not found' % invoke)


    def register(self, cmd_class: command.Command):
        self.registered_commands[cmd_class.get_invoke()] = cmd_class

    def parse_command_stack(self, command_stack: list):
        for command in command_stack:
            self._parse_command(command)