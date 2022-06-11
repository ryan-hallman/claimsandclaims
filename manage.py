from flask.cli import FlaskGroup
import sys
from termcolor import colored

from app import app, db, models

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("runserver")
def runserver():
  manager.run()

if __name__ == '__main__':
    cli()
    #manager.run()
