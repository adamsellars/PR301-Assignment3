from abc import ABCMeta, abstractmethod


class AbstractHelpMessage(metaclass=ABCMeta):
    def __init__(self):
        self.banner = "=====" * 10

    @abstractmethod
    def display_message(self):
        pass
