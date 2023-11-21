# app/routes.py

from flask import Blueprint, render_template, session, redirect, url_for, request
from app.models import Product, BlogPost, Equipment, Cart

bp = Blueprint('main', __name__)

@bp.route('/')
def homepage():
    return render_template('index.html')

@bp.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@bp.route('/cart')
def view_cart():
    cart_contents = []

    # Fetch details for items in the cart
    for key, quantity in session.get('cart', {}).items():
        item_type, item_id = key.split('_')  # Split the string to retrieve type and id

        if item_type == 'product':
            item = Product.query.get(item_id)
        elif item_type == 'equipment':
            item = Equipment.query.get(item_id)
        else:
            # Handle other item types as needed
            item = None

        if item:
            cart_contents.append({
                'item': item,
                'quantity': quantity,
                'image_filename': getattr(item, 'image_filename', None) # Get image filename from the form
            })

    print(" Cart Contents:", cart_contents) # Check cart contents in the console

    # Print session data for debugging
    print("Session Data:", session.get('cart', {}))

    return render_template('cart.html', cart_contents=cart_contents)
