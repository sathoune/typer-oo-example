import abc

import typer


class BaseModule(abc.ABC):

    def __init__(self):
        self.app = typer.Typer()
        self.app.command()(self.hello)

    @abc.abstractmethod
    def hello(self: typer.Context, name: str):
        pass

    def __call__(self):
        self.app()
