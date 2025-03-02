from flask import Blueprint, jsonify, abort, make_response, request
from utils import auth
from .crud import *
from .serializers import city_schema, cities_schema

views = Blueprint("views", __name__)


@views.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@views.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@views.route("/help")
def index():
    return jsonify({"app": "Города"})


@views.route("/", methods=["GET"])
def get_buildings():
    cities = get_all_cities()
    return jsonify({"cities": cities_schema.dump(cities)})


@views.route("/<int:city_id>", methods=["GET"])
def get_one_building(city_id):
    city = get_city(city_id)
    if not city:
        abort(404)
    return jsonify({"city": city_schema.dump(city)})


@views.route("/", methods=["POST"])
@auth.login_required
def create_city():
    if not request.json or "name" not in request.json or "zipcode" not in request.json:
        abort(400)
    city_data = request.get_json()
    city = insert_city(city_data)
    return jsonify({"city": city_schema.dump(city)}), 201


@views.route("/<int:city_id>", methods=["PUT"])
@auth.login_required
def update_city(city_id):
    city = get_city(city_id)
    if (
        (city is None or not request.json)
        or ("name" in request.json and type(request.json["name"]) is not str)
        or ("zipcode" in request.json and type(request.json["zipcode"]) is not float)
    ):
        abort(400)
    city_update = update_city(city_id, request.get_json())
    return jsonify({"city": city_schema.dump(city_update)})


@views.route("/<int:city_id>", methods=["DELETE"])
@auth.login_required
def delete_one_city(city_id):
    result = delete_city(city_id)
    if not result:
        abort(404)
    return jsonify({"result": "True"}), 204
