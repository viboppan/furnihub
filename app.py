from flask import Flask, render_template

from mnop.Customer import customer_endpoints

app = Flask(__name__)
app.register_blueprint(customer_endpoints)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("creativelogin.html")


if __name__ == '__main__':
    app.run(DEBUG=True)
