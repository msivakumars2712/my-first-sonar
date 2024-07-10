from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def Home():
        return {"message": "welcome to my-first-sonar"}

    return app

