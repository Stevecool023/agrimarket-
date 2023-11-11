# app/routes.py

from flask import Blueprint, render_template
from app.models import Product, BlogPost, Equipment

bp = Blueprint('main', __name__)

@bp.route('/')
def homepage():
    return render_template('index.html')

@bp.route('/products')
def products():
    # Fetch products from the database
    products_data = Product.query.all()
    return render_template('products.html', products=products_data)

@bp.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@bp.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment_data = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment_data)

@bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    # Your existing code for adding products
    pass
