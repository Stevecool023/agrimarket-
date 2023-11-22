# routes logic

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from app import db
from app.models import User, BlogPost, Item, Cart
from app.routes import bp

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

# Add more routes as needed for other functionalities
