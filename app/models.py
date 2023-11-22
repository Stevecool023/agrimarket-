# models classes

from datetime import datetime
from flask_login import UserMixin
from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    item_type = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)
    cost = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, item_type={self.item_type}, code={self.code})"

class Product(Item):
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'product'}
    __tablename__ = 'product'

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, code={self.code})"

class Equipment(Item):
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'equipment'}
    __tablename__ = 'equipment'

    def __repr__(self):
        return f"Equipment(id={self.id}, name={self.name}, code={self.code})"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    cart_items = db.relationship('Cart', backref='user', lazy=True)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"BlogPost(id={self.id}, title={self.title}, author_id={self.author_id})"

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    item = db.relationship('Item', backref='cart_item', lazy=True)

    def __repr__(self):
        return f"Cart(id={self.id}, user_id={self.user_id}, item_id={self.item_id}, quantity={self.quantity})"
