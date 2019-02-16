import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:<password>localhost:3306/box_office_db"

db = SQLAlchemy(app)






#################################################
# Flask Routes
#################################################


"""Render Home Page Path"""
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/map1")
def map1():
    return "Yooooo Checkout Our Map!"


@app.route("/data_sources")
def data_sources():
    ## HTML page with data sources links


if __name__ == '__main__':
    app.run(debug=True)
