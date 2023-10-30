from mongoengine import *


class Admin(Document):
    admin_username = StringField()
    email = EmailField()
    password = StringField()
    role = StringField()


# class Customer(Document):
#     username = StringField()
#     email = EmailField()
#     mobile_number = StringField()
#     address = StringField()
#     order_history = ListField(field=ObjectIdField)


class Product(Document):
    name = StringField()
    cost = FloatField()
    dimensions = StringField()
    color = StringField()
    material_type = StringField()
    weight = FloatField()
    rating = FloatField()


class Seller(Document):
    seller_name = StringField()
    email = EmailField()
    contact_number = StringField()
    brand = StringField()
    products = ListField(field=ObjectIdField)


class ProductBought(EmbeddedDocument):
    product_id = ObjectIdField()
    quantity = IntField()


class Order(Document):
    customer_id = ObjectIdField()
    products = EmbeddedDocumentListField(ProductBought)
    order_date = DateField()
    total_cost = FloatField()
    order_status = StringField()


class Payment(Document):
    payment_id = ObjectIdField()
    order_id = ObjectIdField()
    payment_date = DateField()
    payment_method = StringField()
    amount = FloatField()
    status = StringField()
