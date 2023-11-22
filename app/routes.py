# routes logic

from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, login_required, current_user, logout_user
from app import db
from app.models import User, BlogPost, Item, Cart
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    products = Item.query.filter_by(item_type='product').all()
    return render_template('index.html', products=products)

@bp.route('/add_to_cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item = Item.query.get(item_id)
    if item:
        cart_item = Cart(user=current_user, item=item)
        db.session.add(cart_item)
        db.session.commit()
        flash(f"{item.name} added to cart successfully!", 'success')
    else:
        flash("Item not found.", 'danger')
    return redirect(url_for('main.index'))

@bp.route('/view_cart')
@login_required
def view_cart():
    user_cart_items = Cart.query.filter_by(user=current_user).all()
    return render_template('cart.html', cart_items=user_cart_items)

@bp.route('/blog')
def blog():
    # Logic to fetch blog data
    # For example, you might have a list of blog posts
    blog_posts = [
            {"title": "Exploring Sustainable Farming Practices", "date": "November 15, 2023", "image": "images/sustainable-farming.jpg", "content": "Sustainable farming is a holistic approach to agriculture that focuses on preserving the environment, promoting biodiversity, and ensuring long-term food security..."},
            {"title": "The Importance of Crop Rotation", "date": "November 20, 2023", "image": "images/crop-rotation.jpg", "content": "Crop rotation is a key practice in sustainable agriculture. It involves growing different types of crops in the same area in sequential seasons to improve soil health, reduce pests..."},
            {"title": "Boosting Livestock Productivity with Smart Feeding", "date": "November 25, 2023", "image": "images/smart-feeding.jpg", "content": "Smart feeding technologies have revolutionized livestock farming, offering precise nutrition, optimizing feeding schedules, and improving overall productivity. Learn how these innovations are transforming the industry..."},
            # Add more blog posts as needed
    ]

    return render_template('blog.html', blog_posts=blog_posts)

# Add more routes as needed for other functionalities
