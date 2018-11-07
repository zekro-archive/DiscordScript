"""
Command abstract class.
"""

from abc import ABC, abstractmethod, abstractstaticmethod


class Command(ABC):
    def __init__(self, cmd_parser):
        self.cmd_parser = cmd_parser
        super(Command, self).__init__()

    @abstractstaticmethod
    def get_invoke() -> str:
        """
        Returns the invoke to use to execute
        the command.
        """
        pass

    @abstractstaticmethod
    def get_args() -> dict:
        """
        Returns the arguments which can/must be
        passed. The key is the name of the argument
        and the key defines if it is required or not.
        """
        pass

    @abstractstaticmethod
    def get_help_description() -> str:
        pass

    def get_help(self) -> str:
        out = 'USAGE: ' + self.get_invoke() + ' '
        for a in self.get_args():
            key = '[' + a + ']'
            if self.get_args()[a]:
                key = '(' + key + ')'
            out += key + ' '
        return out + '\n\n' + self.get_help_description()
    
    @abstractmethod
    def execute(self, passed_args: list):
        pass