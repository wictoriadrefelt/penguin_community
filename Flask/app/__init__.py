from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

bcrypt = Bcrypt(app)

from app import routes
