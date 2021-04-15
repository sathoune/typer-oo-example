import typer

from many_typers_extended.base_module import BaseModule


class AngryModule(BaseModule):
    def __init__(self):
        super(AngryModule, self).__init__()
        self.secret = 14
        self.register_command(self.expose_secret)
        self.register_command(self.expose_context)

    @staticmethod
    def hello(name: str):
        typer.echo(f"Hello very much, {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f"Goodbye very much, {name}")

    def expose_secret(self):
        typer.echo(f"The secret is: {self.secret}")

    @staticmethod
    def expose_context(ctx: typer.Context):
        typer.echo(f"The command from context is: {ctx.command}")


class YourModule(BaseModule):
    def __init__(self):
        super(YourModule, self).__init__()
        self.register_command(self.custom)
        self.register_command(self.other_custom)

    @staticmethod
    def hello(name: str):
        typer.echo(f"Greetings chap! If I recall correctly you are named {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f'See you later, {name}')

    @staticmethod
    def custom(nickname: str):
        typer.echo(f"Welcome, {nickname}")

    @staticmethod
    def other_custom(nickname: str):
        typer.echo(f"Welcome, {nickname} in the other custom method")
