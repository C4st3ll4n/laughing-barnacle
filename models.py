import enum

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class StatusType(enum.Enum):
    DEACTIVATE = 0
    ANALYSIS = 1
    ACTIVE = 2


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255))
    slug = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=True)
    image = db.Column(db.String(255))
    status = db.Column(db.Enum(StatusType))

    def __repr__(self):
        return f"<book {self.id} {self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "status": self.status,
            "price": self.price,
            "image": self.image,
            "slug": self.slug
        }
