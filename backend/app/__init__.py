import os

from flask import Flask
from flask_cors import CORS

from app.routes import bp
from app.database import db

def create_app() -> Flask:
    app = Flask(__name__)

    CORS(app)

    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app import models

    with app.app_context():
        db.create_all()

    # Register Blueprint
    app.register_blueprint(bp, url_prefix="/api")

    return app
