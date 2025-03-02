from sqlalchemy import func, desc

from utils import db
from models import Customer, Category, City, Product, Employee, Sale
from structures.serializers import city_schema


def get_all_cities():
    query = City.query.all()
    return query


def get_city(city_id):
    query = City.query.filter(City.id == city_id).one_or_none()
    return query


def insert_city(city):
    item = city_schema.load(city, session=db.session)
    db.session.add(item)
    db.session.commit()
    return City.query.filter(
        City.id == db.session.query(func.max(City.id))
    ).one_or_none()


def update_city(city_id, update_par):
    City.query.filter(City.id == city_id).update(update_par)
    db.session.commit()
    building = get_city(city_id)
    return building


def delete_city(city_id):
    City.query.filter(City.id == city_id).delete()
    db.session.commit()
    return True


def get_max_price_product():
    return (
        db.session.query(Product.name, Product.price)
        .order_by(desc(Product.price))
        .first()
    )


def get_min_price_product():
    return db.session.query(Product.name, Product.price).order_by(Product.price).first()


def get_avg_price_per_category():
    return (
        db.session.query(Category.name, func.avg(Product.price))
        .join(Product)
        .group_by(Category.id)
        .all()
    )
