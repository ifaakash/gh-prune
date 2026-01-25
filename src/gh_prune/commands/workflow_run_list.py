import json
import subprocess
import typer
from rich.console import Console
from rich.table import Table

console = Console()

def workflow_run_list(
    repo_name: str = typer.Argument(
        help="Enter the Repository Name in format /OWNER/REPO\n eg: ifaakash/gh-prune"
    ),
    workflow_file_name: str = typer.Argument(help="Enter the workflow name"),
):
    """List the runs of a particular workflow"""
    result = subprocess.run(
        [
            "gh",
            "run",
            "list",
            "--repo",
            repo_name,
            "--workflow",
            workflow_file_name,
            "--json",
            "databaseId,status,conclusion,createdAt",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        console.print(f"[bold red]Workflow run list failed:[/bold red] {result.stderr}")
        raise typer.Exit(code=1)

    runs = json.loads(result.stdout)

    if not runs:
        console.print("[yellow]No runs found.[/yellow]")
        return

    table = Table(title="GitHub Workflow Runs")

    table.add_column("Index", style="dim", width=6)
    table.add_column("ID", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("Created At", style="blue")
    table.add_column("Conclusion", style="cyan", no_wrap=True)

    for idx, run in enumerate(runs):
        table.add_row(
            str(idx + 1),
            str(run["databaseId"]),
            run["status"] or "-",
            run["conclusion"] or "-",
            run["createdAt"],
        )

    console.print(table)
