from flask import Blueprint, request, jsonify
from models._init_ import cleanup, cursor, conn
from services.users_services import prepare_send_data,authenticate_user

users_routes = Blueprint("users_routes", __name__)

@users_routes.route("/register", methods=["POST"])
def send_data():
    data = request.json
    try:
        resp = prepare_send_data(data)
    except Exception as err:
        raise Exception(f"Error occurred while sending the data: {err}")
    finally:
        cleanup()
    return resp

@users_routes.route("/login", methods = ["POST"])
def login():
    data = request.json
    try:
        resp = authenticate_user(data)
    except Exception as err:
        raise Exception(f"Error occured while sending data: {err}")
    finally:
        cleanup()
    return resp