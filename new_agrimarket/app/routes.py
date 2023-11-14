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
    # existing code for adding products
    if request.method == 'POST':
        # Get form data from the request
        name = request.form.get('name')
        description = request.form.get('description')

        # Create a dictionary to represent the product
        product = {'name': name, 'description': description}

        # Check if the 'cart' key exists in the session
        if 'cart' not in session:
            # If not, initialize the cart as an empty list
            session['cart'] = []

        # Add the product to the cart
        session['cart'].append(product)

        # Redirect to the products page
        return redirect(url_for('main.products'))

    # Render the add_product.html template for GET requests
    return render_template('add_product.html')



@bp.route('/add_equipment', methods=['GET', 'POST'])
def add_equipment():
    # code for adding equipment
    if request.method == 'POST':
        # Get form data from the request
        name = request.form.get('name')
        description = request.form.get('description')

        # Create a dictionary to represent the equipment
        equipment = {'name': name, 'description': description}

        # Check if the 'cart' key exists in the session
        if 'cart' not in session:
            # If not, initialize the cart as an empty list
            session['cart'] = []

        # Add the equipment to the cart
        session['cart'].append(equipment)

        # Redirect to the equipment page
        return redirect(url_for('main.equipment'))

    # Render the add_equipment.htl template for GET requests
    return render_template('add_equipment.html')


@bp.route('/add_to_cart/<item_type>/<int:item_id>', methods=['POST'])
def add_to_cart(item_type, item_id):
    # Ensure the 'cart' key exists in the session
    session.setdefault('cart', {})

    # Increment the quantity or set it to 1 if the item is not in the cart
    session['cart'][(item_type, item_id)] = session['cart'].get((item_type, item_id), 0) + 1

    print("Session Data:", session['cart'])  # Add this line for debugging

    if item_type == 'product':
        return redirect(url_for('products'))
    elif item_type == 'equipment':
        return redirect(url_for('equipment'))
    else:
        # Handle other item types as needed
        pass

# Route for adding products to the cart
@bp.route('/add_product_to_cart', methods=['POST'])
def add_product_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    # Get product details from the form submission
    product_id = request.form.get('product_id')  # Replace 'product_id' with the actual field name from your form
    product_name = request.form.get('product_name')
    product_description = request.form.get('product_description')

    # Create a product item dictionary
    product_item = {'type': 'product', 'id': product_id, 'name': product_name, 'description': product_description}

    # Convert the tuple key into a string
    key = f"{product_item['type']}_{product_item['id']}"

    # Add the product item to the cart
    session['cart'][key] = product_item

    # Redirect to the products page or cart page as needed
    return redirect(url_for('main.products'))

# Route for adding equipment to the cart
@bp.route('/add_equipment_to_cart', methods=['POST'])
def add_equipment_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    # Get equipment details from the form submission
    equipment_id = request.form.get('equipment_id')  # Replace 'equipment_id' with the actual field name from your form
    equipment_name = request.form.get('equipment_name')
    equipment_description = request.form.get('equipment_description')

    # Create an equipment item dictionary
    equipment_item = {'type': 'equipment', 'id': equipment_id, 'name': equipment_name, 'description': equipment_description}

    # Convert the tuple key into a string
    key = f"{equipment_item['type']}_{equipment_item['id']}"

    # Add the equipment item to the cart
    session['cart'][key] = equipment_item

    # Redirect to the equipment page or cart page as needed
    return redirect(url_for('main.equipment'))

@bp.route('/cart')
def view_cart():
    cart_contents = []

    # Fetch details for items in the cart
    for key, quantity in session.get('cart', {}).items():
        try:
            item_type, item_id = key.split('_')  # Split the string to retrieve type and id

            if item_type == 'product':
                item = Product.query.get(item_id)
            elif item_type == 'equipment':
                item = Equipment.query.get(item_id)
            else:
                # Handle other item types as needed
                item = None

            if item:
                cart_contents.append({'item': item, 'quantity': quantity})
        except ValueError:
            # Handle cases where the key is not in the expected format
            pass

    return render_template('cart.html', cart_contents=cart_contents)
