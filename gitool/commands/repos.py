import click
from pathlib import Path
from rich.console import Console
from ..core.git import find_all_repos
from ..core.config import get_config, save_config
from ..ui.display import make_repos_table

console = Console()

@click.group()
def repos():
    """Show all Local Repos."""
    pass

@repos.command("list")
def list_repos():
    """Show all repos in a table."""
    cfg = get_config()
    console.print(f"\n[dim]Looking...:[/dim] {cfg['base_path']}\n")
    all_repos = find_all_repos(cfg["base_path"])

    if not all_repos:
        console.print("[yellow]Could not find repos. Use 'gitool repos set-path' to set path.[/yellow]")
        return

    repos_data = []
    for repo in all_repos:
        try:
            repos_data.append({
                "name":        Path(repo.working_dir).name,
                "branch":      repo.active_branch.name,
                "dirty":       repo.is_dirty(untracked_files=True),
                "last_commit": repo.head.commit.message.strip()[:50],
            })
        except Exception:
            continue

    console.print(make_repos_table(repos_data))
    console.print(f"\n[dim]{len(repos_data)} record(s) found[/dim]\n")

@repos.command("status")
def status_repos():
    """Show only repos with pending changes."""
    cfg = get_config()
    all_repos = find_all_repos(cfg["base_path"])
    dirty = [r for r in all_repos if r.is_dirty(untracked_files=True)]

    if not dirty:
        console.print("[green]All OK no pending changes.[/green]")
        return

    console.print(f"\n[yellow]{len(dirty)} modified repo(s):[/yellow]\n")
    for repo in dirty:
        name = Path(repo.working_dir).name
        branch = repo.active_branch.name
        console.print(f"  [cyan]{name}[/cyan]  →  rama: [green]{branch}[/green]")
    console.print()

@repos.command("set-path")
@click.argument("path")
def set_path(path):
    """Configure path to repo."""
    from pathlib import Path as P
    p = P(path)
    if not p.exists():
        console.print(f"[red] Doesnt exist:[/red] {path}")
        return
    cfg = get_config()
    cfg["base_path"] = str(p.resolve())
    save_config(cfg)
    console.print(f"[green]Route saved:[/green] {cfg['base_path']}")