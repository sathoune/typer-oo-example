import typer

from hacky_click_to_typer.base_module import BaseModule


class MyModule(BaseModule):
    def hello(self, name: str):
        typer.echo(f"Hello, {name}")

    def goodbye(self, name: str):
        typer.echo(f"Later! {name}")

class YourModule(BaseModule):
    def hello(self, name: str):
        typer.echo(f"Greetings chap!")

    def goodbye(self: typer.Context, name: str):
        typer.echo("Excuse me Sir, do you now if there is a loo somewhere here?")


YourModule()()
MyModule()()