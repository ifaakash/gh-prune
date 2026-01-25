import json
import subprocess
import typer
from rich.console import Console
from rich.table import Table

console = Console()

def workflow_list(
    repo_name: str = typer.Argument(
        help="Enter the Repository Name in format /OWNER/REPO\n ( e.g. ifaakash/gh-prune )"
    ),
):
    """List workflow in a particular repository"""
    if repo_name is not None:
        result = subprocess.run(
            [
                "gh",
                "workflow",
                "list",
                "--repo",
                repo_name,
                "--json",
                "name,state,id",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            console.print(f"[bold red]Workflow list failed:[/bold red] {result.stderr}")
            raise typer.Exit(code=1)

        workflows = json.loads(result.stdout)

        if not workflows:
            console.print("[yellow]No workflows found.[/yellow]")
            return

        table = Table(title="GitHub Workflows")

        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("State", style="green")
        table.add_column("ID", style="magenta")

        for wf in workflows:
            table.add_row(
                wf["name"],
                wf["state"],
                str(wf["id"]),
            )
        console.print(table)
