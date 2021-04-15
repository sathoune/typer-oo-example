import abc

import typer


class BaseModule(abc.ABC):
    def __init__(self):
        self.app = typer.Typer()

        self.register_command(self.hello)
        self.register_command(self.goodbye)

    @staticmethod
    @abc.abstractmethod
    def hello(name: str):
        pass

    @staticmethod
    @abc.abstractmethod
    def goodbye(name: str):
        pass

    def register_command(self, func):
        self.app.command()(func)

    def run(self):
        self.app()
