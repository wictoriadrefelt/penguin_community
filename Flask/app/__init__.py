from flask import Flask

app = Flask(__name__)
app.config["SECRET KEY"] = "mysecret"

from app import routes