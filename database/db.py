from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = None


def register_db(app: Flask):
    global db
    db = SQLAlchemy(app)

    from . import models

    db.create_all()


def get_db() -> SQLAlchemy:
    return db


def create_tables():
    pass

