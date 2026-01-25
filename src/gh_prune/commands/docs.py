from rich.console import Console
from rich.table import Table

console = Console()


def docs():
    """
    How to use gh-prune
    """
    table = Table(title="gh-prune Documentation")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Example", style="green")

    table.add_row("Install gh", "Install GitHub CLI", "brew install gh")
    table.add_row(
        "Login", "Authenticate with GitHub", "gh auth login --hostname github.com"
    )
    table.add_row(
        "doctor",
        "Health check",
        "python3 doctor.py doctor",
    )
    table.add_row(
        "workflow-list",
        "List workflows",
        "python3 doctor.py workflow-list ifaakash/gh-prune",
    )
    table.add_row(
        "workflow-run-list",
        "List runs of a workflow",
        "python3 doctor.py workflow-run-list ifaakash/gh-prune pylint.yml",
    )
    table.add_row(
        "workflow-run-delete",
        "Delete old workflow runs",
        "python3 doctor.py workflow-run-delete ifaakash/gh-prune cron-workflow.yml --keep 180 --limit 200",
    )
    table.add_row(
        "workflow-run-prune",
        "Delete all workflow runs",
        "python3 doctor.py workflow-run-prune ifaakash/gh-prune cron-workflow.yml --limit 200",
    )

    console.print(table)
