from flask import Blueprint, jsonify  # type: ignore

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"msg": "produto cadastrado com sucesso"}), 200


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"msg": f"Product {product_name}"}), 200
