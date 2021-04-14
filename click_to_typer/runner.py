import typer

from click_to_typer.base_module import BaseModule


class MyModule(BaseModule):
    def hello(self, name: str):
        typer.echo(f"Hello, {name}")


class YourModule(BaseModule):
    def hello(self, name: str):
        typer.echo(f"Greetings chap!")


YourModule()()
MyModule()()
