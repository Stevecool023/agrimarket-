#!/usr/bin/env python3

# add products and equipment

from app import create_app, db
from app.models import Item

app = create_app()

def add_item(name, description, item_type, code=None, image=None, cost=None):
    with app.app_context():
        existing_item = Item.query.filter_by(code=code).first()
        if existing_item:
            # Update existing item
            existing_item.name = name
            existing_item.description = description
            existing_item.image_url = image
            existing_item.cost = cost
        else:
            # Create a new item
            item = Item(name=name, description=description, code=code, image_url=image, cost=cost, item_type=item_type)
            db.session.add(item)

        db.session.commit()

# List of products to add
products_to_add = [
    {"name": "cowbest", "description": "High-quality dairy cow feed.", "code": "CB02", "image": "images/cowbest.jpg", "cost": 20.00},
    {"name": "sheep", "description": "Healthy and well-maintained sheep for your farm.", "code": "SH01", "image": "images/sheep.jpg", "cost": 150.00},
    {"name": "Freshian", "description": "Freshian cattle known for high milk production.", "code": "FR03", "image": "images/Freshian.jpg", "cost": 5000.00},
    {"name": "cowy", "description": "Cowy - A nutritious cow feed for optimal health.", "code": "CW01", "image": "images/cowy.jpg", "cost": 15.00},
    {"name": "eggs", "description": "Fresh and organic eggs from free-range hens.", "code": "EG01", "image": "images/eggs.jpg", "cost": 3.00},
    {"name": "fruity", "description": "Assorted fresh fruits for a healthy lifestyle.", "code": "FTY01", "image": "images/fruity.jpg", "cost": 10.00},
    {"name": "milky", "description": "Pure and fresh milk from happy, well-fed cows.", "code": "MKY01", "image": "images/milky.jpg", "cost": 8.00},
    {"name": "eggssss", "description": "Premium eggs from well-cared-for chickens.", "code": "EGS01", "image": "images/eggssss.jpg", "cost": 5.00},
    {"name": "goatly", "description": "Nutritious goat feed for robust health.", "code": "GT01", "image": "images/goatly.jpg", "cost": 25.00},
    {"name": "ndama", "description": "Ndama cattle known for their hardiness.", "code": "ND01", "image": "images/ndama.jpg", "cost": 4500.00},
    {"name": "sweetpotatoes", "description": "Sweet and nutritious sweet potatoes.", "code": "SP01", "image": "images/sweetpotatoes.jpg", "cost": 2.00},
    {"name": "goaty", "description": "Goaty - Specialized goat feed for optimal growth.", "code": "GY01", "image": "images/goaty.jpg", "cost": 18.00},
    {"name": "onions", "description": "Fresh and high-quality onions for your kitchen.", "code": "ON01", "image": "images/onions.jpg", "cost": 1.50},
    {"name": "veg&fruits", "description": "A variety of fresh vegetables and fruits.", "code": "VF01", "image": "images/veg&fruits.jpg", "cost": 12.00},
    {"name": "vegetables&fruits", "description": "A delightful mix of vegetables and fruits.", "code": "V&F01", "image": "images/vegetables&fruits.jpg", "cost": 15.00},
    {"name": "beansspecies", "description": "Top-quality beans for your agricultural needs.", "code": "BS01", "image": "images/beansspecies.jpg", "cost": 7.00},
    {"name": "hen (1)", "description": "Healthy hens producing quality eggs for your farm.", "code": "HN01", "image": "images/hen (1).jpg", "cost": 8.00},
    {"name": "pig&lets", "description": "Pig feed suitable for both adults and piglets.", "code": "PL01", "image": "images/pig&lets.jpg", "cost": 22.00},
    {"name": "yummy yums", "description": "Yummy Yums - A tasty treat for your animals.", "code": "YY01", "image": "images/yummy yums.jpg", "cost": 3.50},
    {"name": "hen", "description": "Healthy hens providing nutritious eggs for your kitchen.", "code": "HN02", "image": "images/hen.jpg", "cost": 7.00},
    {"name": "piggy", "description": "Piggy - Nutrient-rich feed for healthy pigs.", "code": "PG01", "image": "images/piggy.jpg", "cost": 20.00},
    {"name": "cerially", "description": "Cerially - A complete and balanced cereal mix.", "code": "CR01", "image": "images/cerially.jpg", "cost": 5.00},
    {"name": "farmchems", "description": "Quality farm chemicals for crop protection.", "code": "FC01", "image": "images/farmchems.jpg", "cost": 30.00},
    {"name": "horsy", "description": "Horsy - Premium horse feed for strength and vitality.", "code": "HY01", "image": "images/horsy.jpg", "cost": 25.00},
    {"name": "pigsy", "description": "Pigsy - Specially formulated pig feed for optimal growth.", "code": "PS01", "image": "images/pigsy.jpg", "cost": 18.00},
    {"name": "chicken", "description": "Chicken - Nutritious feed for healthy and happy chickens.", "code": "CK01", "image": "images/chicken.jpg", "cost": 6.00},
    {"name": "maize", "description": "Maize - Essential grain for various culinary uses.", "code": "MZ01", "image": "images/maize.jpg", "cost": 4.00},
    {"name": "potatoes", "description": "Potatoes - Versatile and delicious tubers for your kitchen.", "code": "PT01", "image": "images/potatoes.jpg", "cost": 3.00},
    {"name": "farm machinery", "description": "High-quality farm machinery for efficient agricultural operations.", "code": "FM01", "image": "images/farm machinery.jpg", "cost": 2000.00},
    {"name": "farm tools", "description": "Durable and reliable farm tools for various agricultural tasks.", "code": "FT02", "image": "images/farm tools.jpg", "cost": 50.00},
    {"name": "panga", "description": "A sharp and durable panga, essential for various cutting and clearing tasks on the farm.", "code": "PN01", "image": "images/panga.jpg", "cost": 10.00},
    {"name": "fork&jembe", "description": "An efficient fork & jembe for lifting and turning soil in your garden or field.", "code": "FJ01", "image": "images/fork&jembe.jpg", "cost": 15.00},
    {"name": "mattock", "description": "A versatile mattock for digging and chopping tasks on the farm.", "code": "MT01", "image": "images/mattock.jpg", "cost": 30.00},
    {"name": "farm equipment", "description": "Essential farm equipment for various agricultural operations.", "code": "FE01", "image": "images/farm equipment.jpg", "cost": 500.00},
    {"name": "shovel", "description": "A sturdy shovel for digging and moving soil on the farm.", "code": "SH03", "image": "images/shovel.jpg", "cost": 20.00},
    {"name": "fruits", "description": "Specialized equipment for harvesting and handling fruits on the farm.", "code": "FR01", "image": "images/fruits.jpg", "cost": 100.00},
    {"name": "milk", "description": "Equipment for milk processing and handling on the farm.", "code": "MK01", "image": "images/milk.jpg", "cost": 150.00},
    {"name": "sickle", "description": "Agricultural sickle for cutting and harvesting crops.", "code": "SK01", "image": "images/sickle.jpg", "cost": 12.00},
    {"name": "farmchemicals", "description": "Farm chemicals for crop protection and soil maintenance.", "code": "FC02", "image": "images/farmchemicals.jpg", "cost": 40.00},
    {"name": "fertilizer", "description": "Fertilizer - Essential for promoting healthy plant growth and productivity.", "code": "FTL01", "image": "images/fertilizer.jpg", "cost": 25.00},
]

# Add products to the database
for product_data in products_to_add:
        add_item(product_data["name"], product_data["description"], item_type='product', code=product_data["code"], image=product_data["image"], cost=product_data["cost"])

print("Products added successfully.")
