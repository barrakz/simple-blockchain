from os import path

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "helloplayer"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from core.views import views

    app.register_blueprint(views, url_prefix="/")

    create_database(app)

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created database!")
