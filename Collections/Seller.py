from flask import Blueprint, request, jsonify, render_template
from mongoengine import connect

from Collections.Order import get_orders_for_seller
from utils.MongoDBUtils import Product, Order
from utils.MongoDBUtils import Seller

seller_endpoints = Blueprint('seller_endpoints', __name__, template_folder='templates')
connect(host="mongodb://localhost:27017/furnihub")


def get_seller(username):
    seller = Seller.objects(email=username).first()
    seller_dict = seller_to_dict(seller)
    return seller_dict


def seller_to_dict(seller):
    products_list = [str(product_id) for product_id in seller.products]

    seller_dict = {
        'seller_name': seller.seller_name,
        'email': seller.email,
        'contact_number': seller.contact_number,
        'products': products_list
    }

    return seller_dict


@seller_endpoints.route("/seller/add", methods=['POST'])
def add_user():
    if request.method == 'POST':
        seller_name = request.form.get('username')
        email = request.form.get('email')
        contact_number = request.form.get('contact_number')
        brand = "ikea"
        product_ids = request.form.get('products', [])
        print("hellooooooooooooooooooooooooooooooo")
        # Create a new seller
        new_seller = Seller(
            seller_name=seller_name,
            email=email,
            contact_number=contact_number,
            products=[]
        )
        new_seller.save()
        return render_template('seller.html', ordered_products=get_orders_for_seller(new_seller.id))

    else:
        return "hi"


@seller_endpoints.route('/seller/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        # Check if the user exists
        seller = Seller.objects(seller_name=username).first()
        if seller and seller.password == password:
            print(seller.id)
            ordered_products1 = get_orders_for_seller(str(seller.id))
            print("post order")
            print(ordered_products1)
            return render_template('seller.html', ordered_products=ordered_products1)
        else:
            error = "Invalid username or password. Please try again."
            return render_template('seller_login.html', error=error)

    # return render_template('seller.html')

    # Function to get orders for a given customer


def get_products():
    products = Product.objects()
    products_data = [
        {"name": p.name, "cost": p.cost, "dimensions": p.dimensions, "color": p.color, "brand": p.brand,
         "material": p.material_type, "weight": p.weight, "seller_id": p.seller_id,
         "rating": p.rating, "image_url": p.image_url, "product_id": str(p.id),
         "available_quantity": p.available_quantity, "category": p.category} for p in products]
    return products_data
