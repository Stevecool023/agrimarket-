# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Configure the application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'agrimarket.db')   # SQLite database file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disable Flask-SQLAlchemy modification tracking

    # Initialize SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import and register blueprints
    from app.routes import bp as main_bp  # Import the Blueprint instance
    app.register_blueprint(main_bp)

    return app
