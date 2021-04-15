import typer

from many_typers_extended.my_modules import AngryModule, YourModule


class PapaTyper:
    def __init__(self):
        self.app = typer.Typer()

        my_typers = [
            ("angry", AngryModule()),
            ("classic", YourModule()),
        ]
        for name, subcommand in my_typers:
            self.app.add_typer(subcommand.app, name=name)

    def run(self):
        self.app()
