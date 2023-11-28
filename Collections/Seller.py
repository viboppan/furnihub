from flask import Blueprint, request, jsonify, render_template
from mongoengine import connect

from utils.MongoDBUtils import Seller

seller_endpoints = Blueprint('seller_endpoints', __name__, template_folder='templates')
connect(host="mongodb://localhost:27017/furnihub")


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
            brand=brand,
            products=[]
        )
        new_seller.save()
        return render_template('seller.html')

    else:
        return "hi"


@seller_endpoints.route('/seller/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        seller = Seller.objects(email=username).first()
        # if seller and seller.password == password:
        return render_template('seller.html')
    #     else:
    #         error = "Invalid username or password. Please try again."
    #         return error
    # return render_template('seller.html')

    # Function to get orders for a given customer
