#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Product, BlogPost, Equipment, User

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/products')
def products():
    # Fetch products from the database
    products_data = Product.query.all()
    return render_template('products.html', products=products_data)

@app.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@app.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment_data = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment_data)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Get product details from the form
        name = request.form['name']
        description = request.form['description']

        # Create a new product instance
        new_product = Product(name=name, description=description)

        # Add the product to the database
        db.session.add(new_product)
        db.session.commit()

        # Redirect to the products page after adding the product
        return render_template(url_for('products'))
    
    return render_template('add_products.html')
