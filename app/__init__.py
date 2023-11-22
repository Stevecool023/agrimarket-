# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    # Configure the application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'agrimarket.db')   # SQLite database file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disable Flask-SQLAlchemy modification tracking

    # Initialize SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize Flask-Login
    login_manager = LoginManager(app)
    login_manager.login_view = 'login' # 'login' is the endpoint for my login route

    # Import and register blueprints
    from app.routes import bp as main_bp  # Import the Blueprint instance
    app.register_blueprint(main_bp)

    # Import models
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
