import shutil
import subprocess

import typer
from rich.console import Console

console = Console()


def doctor():
    """
    Check if gh is installed and configured\n
    Check CLI authentication status
    """
    if not shutil.which("gh"):
        console.print("""❌ GitHub CLI not found

        Install it from:
        https://cli.github.com/

        Then run:
        gh auth login""")
        raise typer.Exit(code=1)
    else:
        console.print("[bold green]✅ gh is installed![/bold green]")

    authentication_status = subprocess.run(
        ["gh", "auth", "status"], capture_output=True, text=True
    )
    if authentication_status.returncode != 0:
        console.print(
            f"[bold red]⚠️ CLI authentication status check failed:[/bold red] {authentication_status.stderr}\nThen re-run:\n gh-prune doctor"
        )
        raise typer.Exit(code=1)

    console.print(
        f"[bold green]CLI authentication status:[/bold green]\n{authentication_status.stdout.strip()}"
    )
    console.print(
        "[bold green]✅ GitHub CLI authenticated successfully 🎉[/bold green]"
    )
    console.print("[bold green]✅ Host: github.com[/bold green]")
