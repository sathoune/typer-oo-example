import abc

import typer


class BaseModule(abc.ABC):

    def __init__(self, address, is_capitalism):
        self.app = typer.Typer()
        self.address = address
        self.is_capitalism = is_capitalism

        self.register_command(self.hello)
        self.register_command(self.goodbye)
        self.register_command(self.get_address)
        self.register_command(self.check_capitalism)
        self.register_command(self.self_and_context)

    @staticmethod
    @abc.abstractmethod
    def hello(ctx: typer.Context, name: str):
        pass

    @staticmethod
    @abc.abstractmethod
    def goodbye(name: str):
        pass

    @abc.abstractmethod
    def get_address(self):
        pass

    @abc.abstractmethod
    def check_capitalism(self, act: bool = typer.Option(...)):
        pass

    @abc.abstractmethod
    def self_and_context(self, ctx: typer.Context, name: str):
        pass

    def register_command(self, func):
        self.app.command()(func)

    def run(self):
        self.app()
