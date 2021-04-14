import typer
from typer_example.new_tournament_menu import NewTournamentMenu

class TournamentMenu:
    typer_app = typer.Typer()

    def __init__(self):
        self.typer_app()
        self.print_menu()
        self.user_selection()

    def print_menu(self):
        number = typer.style("1. ", bold=True)
        typer.echo(number + "Commencer un nouveau tournoi")

        number = typer.style("2. ", bold=True)
        typer.echo(number + "Charger un tournoi")

    def user_selection(self):
        selection = typer.prompt("Entrez votre sélection: ")

        if selection == "1":
            self.create_new_tournament()
        else:
            self.user_selection()

    def create_new_tournament(self=None):
        NewTournamentMenu()