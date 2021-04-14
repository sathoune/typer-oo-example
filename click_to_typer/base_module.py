import abc

import typer


class BaseModule(abc.ABC):

    def __init__(self):
        self.app = typer.Typer()

        self.register_command(self.hello)
        self.register_command(self.goodbye)

        # The commented lines below do the same as above.
        # self.app.command()(self.hello)
        # self.app.command()(self.goodbye)

    @staticmethod
    @abc.abstractmethod
    def hello(ctx: typer.Context, name: str):
        """
        Here we are using typer context:

        https://typer.tiangolo.com/tutorial/commands/context/

        """
        pass

    @staticmethod
    @abc.abstractmethod
    def goodbye(name: str):
        pass

    def register_command(self, func):
        self.app.command()(func)

    def run(self):
        self.app()
