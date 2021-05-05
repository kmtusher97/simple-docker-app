from flask import Blueprint, request

user = Blueprint("user", __name__)


@user.route("/")
def home():
    return "asdasdas"
