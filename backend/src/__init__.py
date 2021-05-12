from flask import Flask
from src.user.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix="/api/user")
