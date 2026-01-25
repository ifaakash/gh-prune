import typer

from gh_prune.commands.docs import docs
from gh_prune.commands.doctor import doctor
from gh_prune.commands.workflow_list import workflow_list
from gh_prune.commands.workflow_run_delete import workflow_run_delete
from gh_prune.commands.workflow_run_list import workflow_run_list
from gh_prune.commands.workflow_run_prune import workflow_run_prune

app = typer.Typer()

app.command()(docs)
app.command()(doctor)
app.command()(workflow_list)
app.command()(workflow_run_list)
app.command()(workflow_run_delete)
app.command()(workflow_run_prune)


def main():
    app()
