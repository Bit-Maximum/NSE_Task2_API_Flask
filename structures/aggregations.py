from flask import Blueprint, jsonify, make_response
from .crud import *

views = Blueprint("aggregations", __name__)


@views.route("/max", methods=["GET"])
def max_price_product():
    product = get_max_price_product()
    return jsonify({"name": product[0], "price": float(product[1])})


@views.route("/min", methods=["GET"])
def min_price_product():
    product = get_min_price_product()
    return jsonify({"name": product[0], "price": float(product[1])})


@views.route("/avg", methods=["GET"])
def avg_price_per_category():
    data = get_avg_price_per_category()
    return jsonify(
        {
            "avg_price_per_category": [
                {"category": cat, "avg_price": float(price)} for cat, price in data
            ]
        }
    )
