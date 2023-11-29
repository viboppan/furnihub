from flask import Blueprint, request, jsonify, render_template
from mongoengine import connect

# from Collections.Order import get_orders_for_seller
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
        'brand': seller.brand,
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
            brand=brand,
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
        # if seller and seller.password == password:
        print(seller.id)
        ordered_products1 = get_orders_for_seller(seller.id)
        print("post order")
        return render_template('seller.html', ordered_products=ordered_products1)
    #     else:
    #         error = "Invalid username or password. Please try again."
    #         return error
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


def get_orders_for_seller(seller_id):
    try:
        # Retrieve the products sold by the seller
        print(seller_id + " here")
        seller_products = Product.objects(seller_id=seller_id)
        print(seller_products)
        # Extract product IDs
        product_ids = [str(product.id) for product in seller_products]
        print((product_ids))
        # Retrieve orders containing the seller's products
        orders = Order.objects(products__product_id__in=product_ids, order_status="processing")
        print(orders)
        # Convert orders to a list of dictionaries for JSON serialization
        orders_data = [order_to_dict(order, seller_products) for order in orders]

        return orders_data

    except Exception as e:
        return jsonify({"error": str(e)}), 400


def order_to_dict(order):
    products_list = []
    for product_bought in order.products:
        product_dict = {
            'product_id': str(product_bought.product_id.id),
            'quantity': product_bought.quantity
        }
        products_list.append(product_dict)

    order_dict = {
        'id': str(order.id),
        'customer_id': str(order.customer_id),
        'products': products_list,
        'order_date': order.order_date.strftime('%Y-%m-%d %H:%M:%S'),
        'total_cost': order.total_cost,
        'order_status': order.order_status
    }
    return order_dict


def order_to_dict(order, product_objects):
    products_list = []
    for product_bought in order.products:
        # Find the product object in product_objects list based on product ID
        product_object = next((prod for prod in product_objects if str(prod.id) == str(product_bought.product_id.id)),
                              None)

        if product_object:
            product_dict = {
                'product': {
                    'id': str(product_object.id),
                    'name': product_object.name,
                    'cost': product_object.cost,
                    'dimensions': product_object.dimensions,
                    'color': product_object.color,
                    'brand': product_object.brand,
                    'material_type': product_object.material_type,
                    'weight': product_object.weight,
                    'seller_id': product_object.seller_id,
                    'rating': product_object.rating,
                    'image_url': product_object.image_url,
                    'category': product_object.category,
                    'description': product_object.description,
                    'available_quantity': product_object.available_quantity
                },
                'quantity': product_bought.quantity
            }
            products_list.append(product_dict)

    order_dict = {
        'order_id': str(order.id),
        'customer_id': str(order.customer_id),
        'products': products_list,
        'order_date': order.order_date.strftime('%Y-%m-%d %H:%M:%S'),
        'total_cost': order.total_cost,
        'order_status': order.order_status
    }
    return order_dict
