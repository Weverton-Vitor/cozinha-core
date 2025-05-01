from flask import Flask
from sys import argv

from views import kitchen_bp, supplier_bp

app = Flask(__name__)
app.register_blueprint(kitchen_bp, url_prefix="/kitchens")
app.register_blueprint(supplier_bp, url_prefix="/suppliers")


@app.route("/")
def hello_world():
    return {"message": "hello world"}


debug = "--debug" in argv

app.run(debug=debug)
