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
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
def deploy():
    """
    Run deployment tasks.
    """
    pass