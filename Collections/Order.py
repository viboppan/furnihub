from flask import request, Blueprint, render_template, session, redirect, url_for, jsonify, json
from mongoengine import *
from mongoengine.base.common import get_document
from utils.MongoDBUtils import Customer

order_endpoints = Blueprint('order_endpoints', __name__,
                            template_folder='templates')

connect(host="mongodb://localhost:27017/furnihub")


@order_endpoints.route("/add_order", methods=['POST'])
def add_order():
    try:
        order1 = get_document('Order')
        product1 = get_document('Product')
        order_data = request.get_json()
        products = order_data['products']
        for product in products:
            product_id = product['product_id']
            if not product1.objects(id=product_id).first():
                return jsonify({"error": f"Product with ID {product_id} does not exist"}), 400

        order = order1(**order_data)
        order.save()

        Customer = get_document('Customer')
        customer = Customer.objects(id=order.customer_id).first()
        print("customer found " + customer.mobile_number)
        if customer:
            # Update the customer's order history
            customer.order_history.append(order.id)
            print("before adding ")
            customer.save()
            return jsonify({"message": "Order added successfully!"}), 201
        else:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Order added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
