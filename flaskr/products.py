from flask import make_response, abort
from config import db
from models import Product, ProductSchema


# # "./api/products", GET
def read_all():
    products = Product.query.order_by(Product.name).all()

    product_schema = ProductSchema(many=True)
    data = product_schema.dump(products)
    return data


# # "./api/product/{id}", GET
def read_one(product_id):
    product = Product.query.filter(Product.product_id == product_id).one_or_none()

    if product is not None:
        product_schema = ProductSchema()
        data = product_schema.dump(product)
        return data

    else:
        abort(404, f"Product not found for ID: {product_id}")


# # "./api/products", POST
def create(product):
    name = product.get("name")
    brand = product.get("brand")

    existing_product = (
        Product.query.filter(Product.name == name)
        .filter(Product.brand == brand)
        .one_or_none()
    )

    if existing_product is None:
        schema = ProductSchema()
        new_product = schema.load(product, session=db.session)

        db.session.add(new_product)
        db.session.commit()

        data = schema.dump(new_product)
        return data, 201

    else:
        abort(409, f"Product {name} of Brand {brand} already existis.")


# # "./api/product/{id}", PUT
def update(product_id, product):

    update_product = Product.query.filter(Product.product_id == product_id).one_or_none()
    name = product.get("name")
    brand = product.get("brand")

    existing_product = (
        Product.query.filter(Product.name == name)
        .filter(Product.brand == brand)
        .one_or_none()
    )

    if update_product is None:
        abort(404, f"Product not found for Id: {product_id}")

    elif (existing_product is not None and existing_product.product_id != product_id):
        abort(409, f"Product {name} of Brand {brand} already exists.")

    else:
        schema = ProductSchema()
        update = schema.load(product, session=db.session)

        update.product_id = update_product.product_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_product)
        return data, 200


# # "./api/product/{id}", DELETE
def delete(product_id):

    product = Product.query.filter(Product.product_id == product_id).one_or_none()

    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return make_response(f"Product {product_id} deleted", 200)

    else:
        abort(404, f"Product not found for Id: {product_id}")
