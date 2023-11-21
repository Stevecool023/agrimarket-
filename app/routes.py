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

@bp.route('/add_product_to_cart', methods=['POST'])
def add_product_to_cart():
    try:
        # Get product details from the form submission
        _quantity = int(request.form['quantity'])
        _code = request.form['code']

        # Validate the received values
        if _quantity and _code and request.method == 'POST':
            product = Product.query.filter_by(code=_code).first()

            if product:
                item_array = {
                    product.code: {
                        'name': product.name,
                        'code': product.code,
                        'quantity': _quantity,
                        'price': product.price,
                        'image': product.image,
                        'total_price': _quantity * product.price
                    }
                }

                all_total_price = 0
                all_total_quantity = 0

                session.modified = True

                if 'cart_item' in session:
                    if product.code in session['cart_item']:
                        # Update quantity and total price if the product is already in the cart
                        old_quantity = session['cart_item'][product.code]['quantity']
                        total_quantity = old_quantity + _quantity
                        session['cart_item'][product.code]['quantity'] = total_quantity
                        session['cart_item'][product.code]['total_price'] = total_quantity * product.price
                    else:
                        # Add the product to the cart if it's not already present
                        session['cart_item'].update(item_array)
                else:
                    # Initialize the cart if it doesn't exist
                    session['cart_item'] = item_array

                # Calculate total quantity and price for all items in the cart
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity += individual_quantity
                    all_total_price += individual_price

                session['all_total_quantity'] = all_total_quantity
                session['all_total_price'] = all_total_price

                return redirect(url_for('.products'))
            else:
                return 'Product not found'
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
        return 'Error while adding item to cart'

@bp.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment)

@bp.route('/add_equipment_to_cart', methods=['POST'])
def add_equipment_to_cart():
    try:
        # Get equipment details from the form submission
        _quantity = int(request.form['quantity'])
        _code = request.form['code']

        # Validate the received values
        if _quantity and _code and request.method == 'POST':
            equipment = Equipment.query.filter_by(code=_code).first()

            if equipment:
                item_array = {
                    equipment.code: {
                        'name': equipment.name,
                        'code': equipment.code,
                        'quantity': _quantity,
                        'price': equipment.price,
                        'image': equipment.image,
                        'total_price': _quantity * equipment.price
                    }
                }

                all_total_price = 0
                all_total_quantity = 0

                session.modified = True

                if 'cart_item' in session:
                    if equipment.code in session['cart_item']:
                        # Update quantity and total price if the equipment is already in the cart
                        old_quantity = session['cart_item'][equipment.code]['quantity']
                        total_quantity = old_quantity + _quantity
                        session['cart_item'][equipment.code]['quantity'] = total_quantity
                        session['cart_item'][equipment.code]['total_price'] = total_quantity * equipment.price
                    else:
                        # Add the equipment to the cart if it's not already present
                        session['cart_item'].update(item_array)
                else:
                    # Initialize the cart if it doesn't exist
                    session['cart_item'] = item_array

                # Calculate total quantity and price for all items in the cart
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity += individual_quantity
                    all_total_price += individual_price

                session['all_total_quantity'] = all_total_quantity
                session['all_total_price'] = all_total_price

                return redirect(url_for('.equipment'))
            else:
                return 'Equipment not found'
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
        return 'Error while adding item to cart'

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
