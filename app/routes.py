# app/routes.py

from flask import Blueprint, render_template, session, redirect, url_for, request
from app.models import Product, BlogPost, Equipment, Cart
from app import db
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

@bp.route('/add_product_to_cart', methods=['POST'])
def add_product_to_cart():
    product_code = request.form.get('code')
    quantity = int(request.form.get('quantity', 1))

    # Fetch the product from the database based on the product code
    product = Product.query.filter_by(code=product_code).first()

    if product:
        cart_item = Cart(
            item_type='product',
            item_id=product.id,
            quantity=quantity,
        )

        db.session.add(cart_item)
        db.session.commit()

        return redirect(url_for('main.view_cart'))

    # Handle the case where the product is not found
    return render_template('error.html', error_message='Product not found')

@bp.route('/add_equipment_to_cart', methods=['POST'])
def add_equipment_to_cart():
    equipment_code = request.form.get('code')
    quantity = int(request.form.get('quantity', 1))

    # Fetch the equipment from the database based on the equipment code
    equipment = Equipment.query.filter_by(code=equipment_code).first()

    if equipment:
        cart_item = Cart(
            item_type='equipment',
            item_id=equipment.id,
            quantity=quantity,
        )

        db.session.add(cart_item)
        db.session.commit()

        return redirect(url_for('main.view_cart'))

    # Handle the case where the equipment is not found
    return render_template('error.html', error_message='Equipment not found')

@bp.route('/cart')
def view_cart():
    cart_contents = []

    # Check if 'cart' key exists in the session
    cart_session = session.get('cart', {})

    # Fetch details for items in the cart
    for key, quantity in cart_session.items():
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
                'image_filename': getattr(item, 'image_filename', None),  # Get image filename from the form
            })
        else:
            # Handle the case where the item is not found (deleted, etc.)
            # You may want to remove it from the session or display a message
            pass # Placeholder pass statement.

    print(" Cart Contents:", cart_contents)  # Check cart contents in the console

    # Print session data for debugging
    print("Session Data:", cart_session)

    return render_template('cart.html', cart_contents=cart_contents)
