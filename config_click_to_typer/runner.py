import typer

from config_click_to_typer.base_module import BaseModule


class YourModule(BaseModule):
    def __init__(self, is_capitalism):
        super(YourModule, self).__init__(
            "https://typer.tiangolo.com",
            is_capitalism,
        )

    @staticmethod
    def hello(ctx: typer.Context, name: str):
        print(ctx.command)
        typer.echo(f"Greetings chap! If I recall correctly you are named {name}")

    @staticmethod
    def goodbye(name: str):
        typer.echo(f'See you later, {name}')

    def get_address(self):
        typer.echo(f'Your address is: {self.address}')

    def check_capitalism(self, act: bool = typer.Option(...)):
        if self.is_capitalism:
            if act:
                typer.echo('Capitalism active. Get back to work!')
            else:
                typer.echo('Capitalism active! You better act!')
        else:
            if act:
                typer.echo("Capitalism is not active. Let's make some then!")
            else:
                typer.echo("Lack of Capitalism goes brrrr.")

    def self_and_context(self, ctx: typer.Context, name: str):
        typer.echo(f'{name} invoked: {ctx.command}.')
        if self.is_capitalism:
            typer.echo('Be wary. Capitalism is active.')
        else:
            typer.echo('Please stop this capitalism thing...')


YourModule(False).run()
