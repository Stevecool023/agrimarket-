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

@bp.route('/add_to_cart/<item_type>/<int:item_id>', methods=['POST'])
def add_to_cart(item_type, item_id):
    # Ensure the 'cart' key exists in the session
    session.setdefault('cart', {})

    # Increment the quantity or set it to 1 if the item is not in the cart
    session['cart'][(item_type, item_id)] = session['cart'].get((item_type, item_id), 0) + 1

    if item_type == 'product':
        return redirect(url_for('products'))
    elif item_type == 'equipment':
        return redirect(url_for('equipment'))
    else:
        # Handle other item types as needed
        pass


@bp.route('/cart')
def view_cart():
    cart_contents = []

    # Fetch details for items in the cart
    for (item_type, item_id), quantity in session.get('cart', {}).items():
        if item_type == 'product':
            item = Product.query.get(item_id)
        elif item_type == 'equipment':
            item = Equipment.query.get(item_id)
        else:
            # Handle other item types as needed
            item = None

        if item:
            cart_contents.append({'item': item, 'quantity': quantity})

    return render_template('cart.html', cart_contents=cart_contents)
