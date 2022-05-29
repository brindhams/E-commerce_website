from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'
app.config['SECRET_KEY']='jwkhfciuewhfwzf323f3'
db = SQLAlchemy(app)
bcrypt= Bcrypt(app)

from shop.admin import routes
from shop.products import routes

