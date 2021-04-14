import typer

from click_to_typer.base_module import BaseModule


class YourModule(BaseModule):
    @staticmethod
    def hello(ctx: typer.Context, name: str):
        print(ctx.command)
        typer.echo(f"Greetings chap! If I recall correctly you are named {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f'See you later, {name}')


app = YourModule()
