import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'agrimarket.db')   # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # Disable Flask-SQLAlchemy modification tracking

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import the routes module
from app import routes
