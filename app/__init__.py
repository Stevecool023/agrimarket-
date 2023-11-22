# flask app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets
from flask_login import LoginManager

# Initialize the extensions without binding them to the app
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'agrimarket.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the extensions to the app inside the create_app function
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes import main_bp, auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    from app.models import User  # Import inside the function

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app, db  # Return both app and db

# Import the models after initializing db to avoid circular import
from app.models import Item, User, BlogPost, Cart
