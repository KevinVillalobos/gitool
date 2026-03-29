import click
from rich.console import Console
from ..core.git import get_repo

console = Console()

TIPOS = {
    "1": "feat",
    "2": "fix",
    "3": "chore",
    "4": "docs",
}

@click.group()
def commit():
    """Herramientas para hacer commits."""
    pass

@commit.command("smart")
def smart_commit():
    """Guía para hacer un commit con formato profesional."""
    repo = get_repo()
    if not repo:
        console.print("[red]No estás dentro de un repo Git.[/red]")
        return

    if not repo.is_dirty(untracked_files=True):
        console.print("[yellow]No hay cambios para commitear.[/yellow]")
        return

    console.print("\n[cyan]¿Qué tipo de cambio es?[/cyan]")
    console.print("  [dim]1[/dim] feat   → nueva funcionalidad")
    console.print("  [dim]2[/dim] fix    → corrección de bug")
    console.print("  [dim]3[/dim] chore  → mantenimiento")
    console.print("  [dim]4[/dim] docs   → documentación\n")

    tipo_key = click.prompt("Elige 1-4")
    if tipo_key not in TIPOS:
        console.print("[red]Opción inválida.[/red]")
        return
    tipo = TIPOS[tipo_key]

    scope = click.prompt("¿En qué parte del código? (Enter para omitir)", default="")
    descripcion = click.prompt("¿Qué hiciste en una línea?")

    if scope:
        mensaje = f"{tipo}({scope}): {descripcion}"
    else:
        mensaje = f"{tipo}: {descripcion}"

    console.print(f"\n[dim]→ Commiteando:[/dim] [cyan]{mensaje}[/cyan]\n")

    confirmacion = click.confirm("¿Confirmas?")
    if not confirmacion:
        console.print("[yellow]Cancelado.[/yellow]")
        return

    repo.git.add(".")
    repo.index.commit(mensaje)
    console.print(f"[green]✓ Commit hecho:[/green] {mensaje}\n")