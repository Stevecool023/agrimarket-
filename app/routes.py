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

@bp.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@bp.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment)

# Update add_equipment_to_cart route
@bp.route('/add_equipment_to_cart', methods=['POST'])
def add_equipment_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    # Get equipment details from the form submission
    equipment_id = request.form.get('equipment_id')
    equipment_name = request.form.get('equipment_name')
    equipment_description = request.form.get('equipment_description')

    # Fetch the equipment item from the database
    equipment = Equipment.query.get(equipment_id)

    # Create an equipment item dictionary
    equipment_item = {
        'type': 'equipment',
        'id': equipment_id,
        'name': equipment_name,
        'description': equipment_description,
        'image_filename': getattr(equipment, 'image_filename', None)  # Set image filename
    }

    # Convert the key into a string
    key = f"{equipment_item['type']}_{equipment_item['id']}"

    # Add the equipment item to the cart
    session['cart'][key] = equipment_item

    # Redirect to the equipment page or cart page as needed
    return redirect(url_for('main.equipment'))

# Update add_product_to_cart route
@bp.route('/add_product_to_cart', methods=['POST'])
def add_product_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    # Get product details from the form submission
    product_id = request.form.get('product_id')
    product_name = request.form.get('product_name')
    product_description = request.form.get('product_description')

    # Fetch the product item from the database
    product = Product.query.get(product_id)

    # Create a product item dictionary
    product_item = {
        'type': 'product',
        'id': product_id,
        'name': product_name,
        'description': product_description,
        'image_filename': getattr(product, 'image_filename', None)  # Set image filename
    }

    # Convert the key into a string
    key = f"{product_item['type']}_{product_item['id']}"

    # Add the product item to the cart
    session['cart'][key] = product_item

    # Redirect to the products page or cart page as needed
    return redirect(url_for('main.products'))

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
