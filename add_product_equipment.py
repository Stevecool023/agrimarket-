#!/usr/bin/env python3
# add_product_equipment.py

from app import create_app, db
from app.models import Item

app = create_app()

def add_item(name, description, item_type, cost=None):
    with app.app_context():
        item = Item(name=name, description=description, item_type=item_type, cost=cost)
        db.session.add(item)
        db.session.commit()

# List of products to add
products_to_add = [
    {"name": "cowbest", "description": "High-quality dairy cow feed.", "cost": 20.00},
    {"name": "sheep", "description": "Healthy and well-maintained sheep for your farm.", "cost": 150.00},
    {"name": "Freshian", "description": "Freshian cattle known for high milk production.", "cost": 5000.00},
    {"name": "cowy", "description": "Cowy - A nutritious cow feed for optimal health.", "cost": 15.00},
    {"name": "eggs", "description": "Fresh and organic eggs from free-range hens.", "cost": 3.00},
    {"name": "fruity", "description": "Assorted fresh fruits for a healthy lifestyle.", "cost": 10.00},
    {"name": "milky", "description": "Pure and fresh milk from happy, well-fed cows.", "cost": 8.00},
    {"name": "eggssss", "description": "Premium eggs from well-cared-for chickens.", "cost": 5.00},
    {"name": "goatly", "description": "Nutritious goat feed for robust health.", "cost": 25.00},
    {"name": "ndama", "description": "Ndama cattle known for their hardiness.", "cost": 4500.00},
    {"name": "sweetpotatoes", "description": "Sweet and nutritious sweet potatoes.", "cost": 2.00},
    {"name": "goaty", "description": "Goaty - Specialized goat feed for optimal growth.", "cost": 18.00},
    {"name": "onions", "description": "Fresh and high-quality onions for your kitchen.", "cost": 1.50},
    {"name": "veg&fruits", "description": "A variety of fresh vegetables and fruits.", "cost": 12.00},
    {"name": "vegetables&fruits", "description": "A delightful mix of vegetables and fruits.", "cost": 15.00},
    {"name": "beansspecies", "description": "Top-quality beans for your agricultural needs.", "cost": 7.00},
    {"name": "hen (1)", "description": "Healthy hens producing quality eggs for your farm.", "cost": 8.00},
    {"name": "pig&lets", "description": "Pig feed suitable for both adults and piglets.", "cost": 22.00},
    {"name": "yummy yums", "description": "Yummy Yums - A tasty treat for your animals.", "cost": 3.50},
    {"name": "hen", "description": "Healthy hens providing nutritious eggs for your kitchen.", "cost": 7.00},
    {"name": "piggy", "description": "Piggy - Nutrient-rich feed for healthy pigs.", "cost": 20.00},
    {"name": "cerially", "description": "Cerially - A complete and balanced cereal mix.", "cost": 5.00},
    {"name": "farmchems", "description": "Quality farm chemicals for crop protection.", "cost": 30.00},
    {"name": "horsy", "description": "Horsy - Premium horse feed for strength and vitality.", "cost": 25.00},
    {"name": "pigsy", "description": "Pigsy - Specially formulated pig feed for optimal growth.", "cost": 18.00},
    {"name": "chicken", "description": "Chicken - Nutritious feed for healthy and happy chickens.", "cost": 6.00},
    {"name": "maize", "description": "Maize - Essential grain for various culinary uses.", "cost": 4.00},
    {"name": "potatoes", "description": "Potatoes - Versatile and delicious tubers for your kitchen.", "cost": 3.00},
]

# Add products to the database
for product_data in products_to_add:
    add_item(product_data["name"], product_data["description"], item_type='product', cost=product_data["cost"])

# List of equipment to add
equipment_to_add = [
    {"name": "farm machinery", "description": "High-quality farm machinery for efficient agricultural operations.", "cost": 2000.00},
    {"name": "farm tools", "description": "Durable and reliable farm tools for various agricultural tasks.", "cost": 50.00},
    {"name": "panga", "description": "A sharp and durable panga, essential for various cutting and clearing tasks on the farm.", "cost": 10.00},
    {"name": "fork&jembe", "description": "An efficient fork & jembe for lifting and turning soil in your garden or field.", "cost": 15.00},
    {"name": "mattock", "description": "A versatile mattock for digging and chopping tasks on the farm.", "cost": 30.00},
    {"name": "farm equipment", "description": "Essential farm equipment for various agricultural operations.", "cost": 500.00},
    {"name": "shovel", "description": "A sturdy shovel for digging and moving soil on the farm.", "cost": 20.00},
    {"name": "fruits", "description": "Specialized equipment for harvesting and handling fruits on the farm.", "cost": 100.00},
    {"name": "milk", "description": "Equipment for milk processing and handling on the farm.", "cost": 150.00},
    {"name": "sickle", "description": "Agricultural sickle for cutting and harvesting crops.", "cost": 12.00},
    {"name": "farmchemicals", "description": "Farm chemicals for crop protection and soil maintenance.", "cost": 40.00},
    {"name": "fertilizer", "description": "Fertilizer - Essential for promoting healthy plant growth and productivity.", "cost": 25.00},
]

# Add equipment to the database
for equipment_data in equipment_to_add:
    add_item(equipment_data["name"], equipment_data["description"], item_type='equipment', cost=equipment_data["cost"])

print("Products and equipment added successfully.")
