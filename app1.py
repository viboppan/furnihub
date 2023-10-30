from flask import Flask, render_template

from Collections.Customer import customer_endpoints
from utils.mongo_setup import insert_sample_data

app1 = Flask(__name__)
app1.register_blueprint(customer_endpoints)


@app1.route('/')
def hello_world():  # put application's code here
    return render_template("creativelogin.html")


if __name__ == '__main__':
    print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #insert_sample_data()
    app1.run(debug=True)
