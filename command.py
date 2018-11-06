"""
Command abstract class.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self):
        super(Command, self).__init__()

    @abstractmethod
    def get_invoke(self) -> str:
        pass

    @abstractmethod
    def get_args(self) -> list:
        pass
    
    @abstractmethod
    def execute(self, passed_args: list):
        pass