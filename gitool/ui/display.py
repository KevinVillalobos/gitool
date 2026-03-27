from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

def make_repos_table(repos_data: list[dict]) -> Table:
    table = Table(title="[bold cyan]Tus repositorios[/bold cyan]")
    table.add_column("Repo",          style="cyan",  min_width=20)
    table.add_column("Rama",          style="green", min_width=12)
    table.add_column("Cambios",       justify="center", min_width=8)
    table.add_column("Último commit", style="dim",   min_width=35)

    for r in repos_data:
        cambios = Text("● sí", style="yellow") if r["dirty"] else Text("—", style="dim")
        table.add_row(r["name"], r["branch"], cambios, r["last_commit"])

    return table