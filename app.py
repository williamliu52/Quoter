from os import environ, path
from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack

import requests

here = path.abspath(path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

webpack = Webpack()
app.config["WEBPACK_MANIFEST_PATH"] = path.join(here, "manifest.json")
webpack.init_app(app)

from models import *
from getStocks import *

queryStocks()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/assets/<path:filename>")
# def send_asset(filename):
#     return send_from_directory(path.join(here, "public"), filename)

if __name__ == '__main__':
    app.run(extra_files=[app.config["WEBPACK_MANIFEST_PATH"]])
