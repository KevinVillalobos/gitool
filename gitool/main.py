import click
from .commands.repos import repos
from .commands.commit import commit

@click.group()
def cli():
    """gitool — tu CLI personal de Git."""
    pass

cli.add_command(repos)
cli.add_command(commit)