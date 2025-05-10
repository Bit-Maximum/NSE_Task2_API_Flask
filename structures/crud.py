from sqlalchemy import func, desc, Integer, cast, case

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


def get_full_price_stats_per_category():
    return (
        db.session.query(
            Category.name.label('category_name'),
            func.min(Product.price).label('min_price'),
            func.avg(Product.price).label('avg_price'),
            func.max(Product.price).label('max_price')
        )
        .join(Product)
        .group_by(Category.id)
        .all()
    )


def get_full_price_stats_per_city():
    return (
        db.session.query(
            City.name.label('city_name'),
            func.min(Product.price).label('min_price'),
            func.avg(Product.price).label('avg_price'),
            func.max(Product.price).label('max_price')
        )
        .join(Customer, Customer.city_id == City.id)
        .join(Sale, Sale.customer_id == Customer.id)
        .join(Product, Product.id == Sale.product_id)
        .group_by(City.id)
        .all()
    )


def get_full_price_stats_per_employee():
    return (
        db.session.query(
            Employee.last_name.label('employee_name'),
            func.min(Product.price).label('min_price'),
            func.avg(Product.price).label('avg_price'),
            func.max(Product.price).label('max_price')
        )
        .join(Sale, Sale.sale_person_id == Employee.id)
        .join(Product, Product.id == Sale.product_id)
        .group_by(Employee.id)
        .all()
    )


def get_price_stats_by_vitality_ranges():
    vitality_ranges = case(
        (Product.vitality_days < 7, "0-6 days"),
        (Product.vitality_days.between(7, 14), "7-14 days"),
        (Product.vitality_days.between(15, 30), "15-30 days"),
        (Product.vitality_days > 30, "30+ days"),
        else_="Unknown"
    ).label("vitality_range")

    return (
        db.session.query(
            vitality_ranges,
            func.min(Product.price).label('min_price'),
            func.avg(Product.price).label('avg_price'),
            func.max(Product.price).label('max_price'),
            func.count(Product.id).label('product_count')
        )
        .filter(Product.vitality_days.isnot(None))
        .group_by(vitality_ranges)
        .order_by(vitality_ranges)
        .all()
    )


def get_price_stats_by_vitality():

    return (
        db.session.query(
            cast(Product.vitality_days, Integer).label('vitality_days'),
            func.min(Product.price).label('min_price'),
            func.avg(Product.price).label('avg_price'),
            func.max(Product.price).label('max_price'),
        )
        .filter(Product.vitality_days.isnot(None))
        .group_by(Product.vitality_days)
        .order_by(Product.vitality_days)
        .all()
    )
