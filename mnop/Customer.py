from flask import request, Blueprint, render_template, session, redirect, url_for
from mongoengine import *

customer_endpoints = Blueprint('customer_endpoints', __name__,
                               template_folder='templates')
connect(host="mongodb://localhost:27017/customer")


class Customer(Document):
    username = StringField()
    email = EmailField()
    password = StringField()
    mobile_number = StringField()
    address = StringField()
    order_history = ListField(field=ObjectIdField)


@customer_endpoints.route("/customer/add", methods=['POST'])
def add_user():
    if request.method == 'POST':
        customer = Customer(username=request.form.get('username'),
                            email=request.form.get('email'),
                            password=request.form.get('password'),
                            mobile_number=request.form.get('phone'))
        customer.save()
        return render_template('homepage.html')
    else:
        print('')


@customer_endpoints.route('/customer/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        customer = Customer.objects(username=username).first()

        if customer and customer.password == password:

            # If username and password are correct, set a session variable
            # session['username'] = username
            return render_template('homepage.html')
        else:
            error = "Invalid username or password. Please try again."
            return error

    return render_template('login.html')


@customer_endpoints.route('/dashboard')
def dashboard():
    return 'This is the dashboard.'
