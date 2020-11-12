import os
import click
from app import create_app, database
from app.models import DailymailColumn

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    """
    Ensures returned values are accessible in the interactive shell
    without importing them.

    :return: a dictionary of values to be imported
    """
    return dict(db=database, DailymailColumn=DailymailColumn)

@app.cli.command()
def deploy():
    """
    Run deployment tasks.

    :return: None
    """
    database.create_all()