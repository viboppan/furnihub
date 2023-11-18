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

            # if product_quantity > product.available_quantity:
            #     return jsonify({"error": f"Not enough stock available for product with ID {product_id}"}), 400

            # Create ProductBought instance
            product_bought_instance = ProductBought(product_id=product_id, quantity=product_quantity)
            product_bought_instances.append(product_bought_instance)

        # Calculate total cost
        total_cost = sum(product_info.get('quantity', 0) * product_info.get('unit_price', 0)
                         for product_info in order_data.get('products', []))

        # Create the order instance
        order = Order(
            customer_id=order_data.get('customer_id'),
            products=product_bought_instances,
            total_cost=total_cost,
        )
        order.save()

        # Update the product available quantity
        # for product_bought_instance in product_bought_instances:
        #     product_id = product_bought_instance.product_id
        #     product_quantity = product_bought_instance.quantity
        #     product = product1.objects(id=product_id).first()
        #     if product:
        #         product.available_quantity -= product_quantity
        #         product.save()

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
