from flask import Blueprint, jsonify, request

from app.create_app import db
from app.database.models import Product
from app.schemas import product_schema, products_schema

bp = Blueprint("products", __name__, url_prefix="/")

# Get all products
@bp.route("/products", methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result)


# Create product
@bp.route("/product", methods=["POST"])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    quantity = request.json["quantity"]

    new_product = Product(name, description, price, quantity)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get a specific product
@bp.route("/product/<id>", methods=["GET"])
def get_product(id):
    product = Product.query.get(id)

    return product_schema.jsonify(product)


# Update product
@bp.route("/product/<id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    quantity = request.json["quantity"]

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()

    return product_schema.jsonify(product)


# Delete product
@bp.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)
