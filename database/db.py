from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = None


def register_db(app: Flask, this_db=None):
    global db

    db = SQLAlchemy(app) if this_db is None else this_db

    from . import models

    db.create_all()


def get_db() -> SQLAlchemy:
    return db


def create_tables():
    pass

