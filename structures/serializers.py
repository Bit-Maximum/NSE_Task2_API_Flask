from models import Category, City, Customer, Employee, Sale, Product
from utils import ma, db


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        sqla_session = db.session

    city = ma.Nested(CitySchema())
    city_id = ma.auto_field()


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
        sqla_session = db.session

    city = ma.Nested(CitySchema())
    city_id = ma.auto_field()


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session

    category = ma.Nested(CategorySchema())
    category_id = ma.auto_field()


class SaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sale
        load_instance = True
        sqla_session = db.session

    sale_persons = ma.Nested(EmployeeSchema())
    customers = ma.Nested(CustomerSchema())
    products = ma.Nested(ProductSchema())

    sale_person_id = ma.auto_field()
    customer_id = ma.auto_field()
    product_id = ma.auto_field()


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
