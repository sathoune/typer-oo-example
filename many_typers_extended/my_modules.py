import typer

from many_typers_extended.base_module import BaseModule


class AngryModule(BaseModule):
    def __init__(self):
        super(AngryModule, self).__init__()
        self.secret = 14
        self.register_many([
            self.expose_secret,
            self.expose_context,
            self.call_everything,
        ])

        # add some nesting with `sub` command.
        self.app.add_typer(YourModule().app, name='sub')

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

    def call_everything(self, ctx: typer.Context, name: str):
        self.hello(name)
        self.expose_secret()
        self.expose_context(ctx)
        self.goodbye(name)


class YourModule(BaseModule):
    def __init__(self):
        super(YourModule, self).__init__()
        self.register_many([
            self.custom,
            self.other_custom,
        ])

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
