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


@views.route("/stats/<group_by>", methods=["GET"])
def get_full_price_stats(group_by):
    if group_by == 'category':
        data = get_full_price_stats_per_category()
        key_name = 'category_name'
        response_key = 'category'
    elif group_by == 'city':
        data = get_full_price_stats_per_city()
        key_name = 'city_name'
        response_key = 'city'
    elif group_by == "vitality":
        data = get_price_stats_by_vitality()
        key_name = 'vitality_days'
        response_key = "category_name"
    elif group_by == 'employee':
        data = get_full_price_stats_per_employee()
        key_name = 'employee_name'
        response_key = 'employee'
    else:
        return jsonify({"error": "Invalid group by parameter"}), 400

    result = {
        f"stats": [
            {
                "Группа": getattr(item, key_name),
                "Минимальная цена": float(item.min_price),
                "Средняя цена": float(item.avg_price),
                "Максимальная цена": float(item.max_price)
            } for item in data
        ]
    }
    return jsonify(result)
