"""
Command abstract class.
"""

from abc import ABC, abstractmethod, abstractstaticmethod


class Command(ABC):
    def __init__(self):
        super(Command, self).__init__()

    @abstractstaticmethod
    def get_invoke() -> str:
        """
        Returns the invoke to use 
        """
        pass

    @abstractstaticmethod
    def get_args() -> dict:
        pass

    @abstractstaticmethod
    def get_help_description() -> str:
        pass

    def get_help(self) -> str:
        return self.get_invoke() + ' '
    
    @abstractmethod
    def execute(self, passed_args: list):
        pass