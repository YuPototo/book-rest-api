from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import app_config


db = SQLAlchemy()
migrate = Migrate()


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)

    from app.resources.book import Book, Booklist

    api.add_resource(Booklist, '/books')
    api.add_resource(Book, '/book/<string:title>')

    return app
