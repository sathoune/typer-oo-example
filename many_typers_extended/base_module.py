import abc
from collections import Callable
from typing import List

import typer


class BaseModule(abc.ABC):
    def __init__(self):
        self.app = typer.Typer()
        self.register_many([
            self.hello,
            self.goodbye
        ])
    @staticmethod
    @abc.abstractmethod
    def hello(name: str):
        pass

    @staticmethod
    @abc.abstractmethod
    def goodbye(name: str):
        pass

    def register_command(self, func: Callable):
        self.app.command()(func)

    def register_many(self, funcs: List[Callable]):
        for func in funcs:
            self.register_command(func)

    def run(self):
        self.app()
