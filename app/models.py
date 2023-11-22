#!/usr/bin/env python3

from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, text

class Item(db.Model):
    __tablename__= 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    item_type = db.Column(db.String(50), nullable=False)  # 'product' or 'equipment'
    cost = db.Column(db.Float)

    __mapper_args__ = {
            'polymorphic_identity': 'item',
            'polymorphic_on': item_type
    }

class Product(Item):
    __tablename__ = 'product'
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    image_url = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {
            'polymorphic_identity': 'product',
    }

class Equipment(Item):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    code = db.Column(db.String(255), nullable=False, unique=True)
    image_url = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {
            'polymorphic_identity': 'equipment',
    }

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_type = db.Column(db.String(50), nullable=False)  # 'product' or 'equipment'
    item_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
