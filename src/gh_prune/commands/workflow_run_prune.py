import json
import subprocess
import typer
from rich.console import Console

console = Console()

def workflow_run_prune(
    repo_name: str = typer.Argument(
        help="Repository in OWNER/REPO format (e.g. ifaakash/gh-pruner)"
    ),
    workflow_file_name: str = typer.Argument(help="Workflow file name (e.g. ci.yml)"),
    limit: int = typer.Option(
        30,
        "--limit",
        help="Number of workflow runs to fetch",
    ),
    yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Skip confirmation prompt",
    ),
):
    """Cleanup workflow and remove from Github Action list"""

    result = subprocess.run(
        [
            "gh",
            "run",
            "list",
            "--repo",
            repo_name,
            "--workflow",
            workflow_file_name,
            "--limit",
            str(limit),
            "--json",
            "databaseId,createdAt",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        console.print("[bold red]Failed to fetch workflow runs[/bold red]")
        console.print(result.stderr)
        raise typer.Exit(code=1)

    runs = json.loads(result.stdout)
    # print(runs)

    console.print(f"[yellow]About to delete {len(runs)} workflow runs[/yellow]")

    for run in runs:
        console.print(f"  • Run ID {run['databaseId']} (created {run['createdAt']})")

    if not yes:
        confirm = typer.confirm("Proceed with deletion?")
        if not confirm:
            console.print("[cyan]Aborted[/cyan]")
            raise typer.Exit()

    for run in runs:
        console.print(f"🗑️  Deleting run {run['databaseId']}")
        delete = subprocess.run(
            [
                "gh",
                "api",
                f"repos/{repo_name}/actions/runs/{run['databaseId']}",
                "-X",
                "DELETE",
            ],
            capture_output=True,
            text=True,
        )

        if delete.returncode != 0:
            console.print(
                f"[bold red]Failed to delete run {run['databaseId']}[/bold red]"
            )
            console.print(delete.stderr)

    console.print(f"[bold green]✅ Deleted {len(runs)} workflow runs[/bold green]")
