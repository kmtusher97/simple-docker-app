from flask import Flask
from src.user.urls import user

app = Flask(__name__)

app.register_blueprint(user, url_prefix="/api/user")
