from flask import Flask
from sys import argv

from routes import kitchen_bp, supplier_bp, order_bp, product_bp

app = Flask(__name__)
app.register_blueprint(kitchen_bp, url_prefix="/kitchens")
app.register_blueprint(supplier_bp, url_prefix="/suppliers")
app.register_blueprint(order_bp, url_prefix="/orders")
app.register_blueprint(product_bp, url_prefix="/products")


@app.route("/")
def hello_world():
    return {"message": "hello world"}


debug = "--debug" in argv

app.run(debug=debug)
