# app/routes.py

from flask import Blueprint, render_template, session, redirect, url_for, request
from app.models import Product, BlogPost, Equipment, Cart

bp = Blueprint('main', __name__)

@bp.route('/')
def homepage():
    return render_template('index.html')

@bp.route('/products')
def products():
    # Fetch products from the database
    products = Product.query.all()
    return render_template('products.html', products=products)

@bp.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment)

@bp.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@bp.route('/cart')
def view_cart():
    cart_contents = []
