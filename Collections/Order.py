from flask import request, Blueprint, render_template, session, redirect, url_for, jsonify, json
from mongoengine import *
from mongoengine.base.common import get_document
from utils.MongoDBUtils import Customer, Order, ProductBought

order_endpoints = Blueprint('order_endpoints', __name__,
                            template_folder='templates')

connect(host="mongodb://localhost:27017/furnihub")


@order_endpoints.route("/add_order", methods=['POST'])
def add_order():
    try:
        order_data = request.get_json()

        # Validate product existence and gather product details
        product1 = get_document('Product')
        product_bought_instances = []
        for product_info in order_data.get('products', []):
            product_id = product_info.get('product_id')
            product_quantity = product_info.get('quantity', 0)

            product = product1.objects(id=product_id).first()
            if not product:
                return jsonify({"error": f"Product with ID {product_id} does not exist"}), 400

            if product_quantity > product.available_quantity:
                return jsonify({"error": f"Not enough stock available for product with ID {product_id}"}), 400
            else:
                product.available_quantity -= product_quantity
                product.save()
            # Create ProductBought instance
            product_bought_instance = ProductBought(product_id=product_id, quantity=product_quantity)
            product_bought_instances.append(product_bought_instance)

        # Calculate total cost
        total_cost = order_data.get('total_cost')

        # Create the order instance
        order = Order(
            customer_id=order_data.get('customer_id'),
            products=product_bought_instances,
            total_cost=total_cost,
        )
        order.save()

        # Update the customer's order history
        customer = Customer.objects(id=order.customer_id).first()
        if customer:
            customer.order_history.append(order.id)
            customer.save()

            return jsonify({"message": "Order added successfully!"}), 201
        else:
            return jsonify({"error": "Customer not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@order_endpoints.route("/get_order/<order_id>", methods=['GET'])
def get_order(order_id):
    try:
        # Retrieve the order based on the order ID
        order = Order.objects(id=order_id).first()

        if order:
            # Convert the order object to a dictionary for JSON serialization
            order_data = order_dict = order_to_dict(order)
            return jsonify(order_data), 200
        else:
            return jsonify({"error": f"Order with ID {order_id} not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@order_endpoints.route("/get_orders_for_seller/<seller_id>", methods=['GET'])
def get_orders_for_seller(seller_id):
    try:
        # Retrieve the products sold by the seller
        seller_products = Product.objects(seller_email=seller_id).only('id')

        # Extract product IDs
        product_ids = [str(product.id) for product in seller_products]

        # Retrieve orders containing the seller's products
        orders = Order.objects(products__product_id__in=product_ids)

        # Convert orders to a list of dictionaries for JSON serialization
        orders_data = [order_to_dict(order) for order in orders]

        return jsonify(orders_data), 200

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
        'customer_id': str(order.customer_id),
        'products': products_list,
        'order_date': order.order_date.strftime('%Y-%m-%d %H:%M:%S'),
        'total_cost': order.total_cost,
        'order_status': order.order_status
    }
    return order_dict