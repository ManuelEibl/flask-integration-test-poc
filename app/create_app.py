from flask import Flask

from app.database.base import db
from app.database.models import *


def init_app(environ: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"app.config.{environ.capitalize()}")
    return app


def init_db(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app: Flask):
    from app.resources import bp

    app.register_blueprint(bp)


def create_app(environ: str) -> Flask:
    app = init_app(environ)
    init_db(app)
    register_blueprints(app)

    return app
