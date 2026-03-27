import click
from .commands.repos import repos

@click.group()
def cli():
    """gitool — tu CLI personal de Git."""
    pass

cli.add_command(repos)