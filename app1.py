from flask import Flask, render_template
from flask_cors import CORS
from Collections.Customer import customer_endpoints
from Collections.Order import order_endpoints
from Collections.Payment import payment_endpoints
from Collections.Product import product_endpoints
from Collections.Seller import seller_endpoints

app1 = Flask(__name__)
CORS(app1)
app1.register_blueprint(customer_endpoints)
app1.register_blueprint(order_endpoints)
app1.register_blueprint(payment_endpoints)
app1.register_blueprint(seller_endpoints)
app1.register_blueprint(product_endpoints)


@app1.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

@app1.route('/')
def hello_world():  # put application's code here
    return render_template("creativelogin.html")


@app1.route('/customer/cart_page')
def cart_page():  # put application's code here
    return render_template("cart_page.html")


@app1.route('/customer/payment_page')
def payment_page():  # put application's code here
    return render_template("payment_page.html")


@app1.route('/customer/order_summary')
def order_summary_page():  # put application's code here
    return render_template("order_summary.html")


if __name__ == '__main__':
    print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    # insert_sample_data()
    app1.run(debug=True)
