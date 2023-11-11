#!/usr/bin/env python3
# script_add_products.py

from app import db
from app.models import Product

# Create the flask app and ensure it uses the correct configuration.
app = create_app()

def add_product(name, description):
    with app.app_context():
        product = Product(name=name, description=description)
        db.session.add(product)
        db.session.commit()

# List of products to add
products_to_add = [
    {"name": "cowbest", "description": "High-quality dairy cow feed."},
    {"name": "sheep", "description": "Healthy and well-maintained sheep for your farm."},
    {"name": "Freshian", "description": "Freshian cattle known for high milk production."},
    {"name": "cowy", "description": "Cowy - A nutritious cow feed for optimal health."},
    {"name": "eggs", "description": "Fresh and organic eggs from free-range hens."},
    {"name": "fruity", "description": "Assorted fresh fruits for a healthy lifestyle."},
    {"name": "milky", "description": "Pure and fresh milk from happy, well-fed cows."},
    {"name": "eggssss", "description": "Premium eggs from well-cared-for chickens."},
    {"name": "goatly", "description": "Nutritious goat feed for robust health."},
    {"name": "ndama", "description": "Ndama cattle known for their hardiness."},
    {"name": "sweetpotatoes", "description": "Sweet and nutritious sweet potatoes."},
    {"name": "goaty", "description": "Goaty - Specialized goat feed for optimal growth."},
    {"name": "onions", "description": "Fresh and high-quality onions for your kitchen."},
    {"name": "veg&fruits", "description": "A variety of fresh vegetables and fruits."},
    {"name": "vegetables&fruits", "description": "A delightful mix of vegetables and fruits."},
    {"name": "beansspecies", "description": "Top-quality beans for your agricultural needs."},
    {"name": "hen (1)", "description": "Healthy hens producing quality eggs for your farm."},
    {"name": "pig&lets", "description": "Pig feed suitable for both adults and piglets."},
    {"name": "yummy yums", "description": "Yummy Yums - A tasty treat for your animals."},
    {"name": "hen", "description": "Healthy hens providing nutritious eggs for your kitchen."},
    {"name": "piggy", "description": "Piggy - Nutrient-rich feed for healthy pigs."},
    {"name": "cerially", "description": "Cerially - A complete and balanced cereal mix."},
    {"name": "farmchems", "description": "Quality farm chemicals for crop protection."},
    {"name": "horsy", "description": "Horsy - Premium horse feed for strength and vitality."},
    {"name": "pigsy", "description": "Pigsy - Specially formulated pig feed for optimal growth."},
    {"name": "chicken", "description": "Chicken - Nutritious feed for healthy and happy chickens."},
    {"name": "maize", "description": "Maize - Essential grain for various culinary uses."},
    {"name": "potatoes", "description": "Potatoes - Versatile and delicious tubers for your kitchen."},
]

# Add products to the database
for product_data in products_to_add:
    add_product(product_data["name"], product_data["description"])

# List of equipment to add
equipment_to_add = [
    {"name": "farm machinery", "description": "High-quality farm machinery for efficient agricultural operations."},
    {"name": "farm tools", "description": "Durable and reliable farm tools for various agricultural tasks."},
    {"name": "panga", "description": "A sharp and durable panga, essential for various cutting and clearing tasks on the farm."},
    {"name": "fork&jembe", "description": "An efficient fork & jembe for lifting and turning soil in your garden or field."},
    {"name": "mattock", "description": "A versatile mattock for digging and chopping tasks on the farm."},
    {"name": "farm equipment", "description": "Essential farm equipment for various agricultural operations."},
    {"name": "shovel", "description": "A sturdy shovel for digging and moving soil on the farm."},
    {"name": "fruits", "description": "Specialized equipment for harvesting and handling fruits on the farm."},
    {"name": "milk", "description": "Equipment for milk processing and handling on the farm."},
    {"name": "sickle", "description": "Agricultural sickle for cutting and harvesting crops."},
    {"name": "farmchemicals", "description": "Farm chemicals for crop protection and soil maintenance."},
    {"name": "fertilizer", "description": "Fertilizer - Essential for promoting healthy plant growth and productivity."},
]

# Add equipment to the database
for equipment_data in equipment_to_add:
    add_product(equipment_data["name"], equipment_data["description"])

print("Products and equipment added successfully.")
