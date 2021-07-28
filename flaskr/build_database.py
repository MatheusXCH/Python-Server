import os
from config import db
from models import Product

# # Objetos iniciados ao criar o database
PRODUCTS = [
    {"name": "Samsung Galaxy S11", "brand": "Samsung", "price": 3400.00, "stock": 150},
    {"name": "Samsung Galaxy M21s", "brand": "Samsung", "price": 1400.00, "stock": 1150},
    {"name": "Redmi Note 10 Pro", "brand": "Xiaomi", "price": 2100.00, "stock": 240}
]

# # Exclui o database, caso já exista um na pasta raíz do projeto
if os.path.exists("products.db"):
    os.remove("products.db")

# # Cria o database e adiciona os objetos iniciais
db.create_all()
for product in PRODUCTS:
    p = Product(
        name=product.get("name"),
        brand=product.get("brand"),
        price=product.get("price"),
        stock=product.get("stock")
    )
    db.session.add(p)

db.session.commit()
