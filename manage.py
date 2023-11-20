#!/usr/bin/env python3

from flask_migrate import Migrate
from flask.cli import FlaskGroup
from app import create_app, db

app = create_app()
migrate = Migrate(app, db)
cli = FlaskGroup(create_app=create_app)

cli.add_command("db", Migrate)

if __name__ == '__main__':
    cli()
