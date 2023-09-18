from flask import Flask
from routes.users import users_routes
#Initialize flask app

app = Flask(__name__)

app.register_blueprint(users_routes)


if __name__ == "__main__":
    app.run()