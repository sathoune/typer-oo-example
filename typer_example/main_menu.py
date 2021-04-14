import typer
from typer_example.tournament_menu import TournamentMenu

class MainMenu:
    typer_app = typer.Typer()
    typer_app.add_typer(TournamentMenu.typer_app, name="tournament")

    def __init__(self):
        self.typer_app()
        self.tournament_handler = None
        self.print_menu()
        self.user_selection()

    def print_menu(self):
        number = typer.style("1. ", bold=True)
        typer.echo(number + "Tournois")

        number = typer.style("2. ", bold=True)
        typer.echo(number + "Gérer les joueurs")

    def user_selection(self):
        selection = typer.prompt("Entrez votre sélection: ")
        typer.echo("\n")

        if selection == "1":
            self.open_tournament_menu()
        else:
            self.user_selection()

    def open_tournament_menu(self):
        TournamentMenu()