from flask import Blueprint
frontend_app = Blueprint('frontend', __name__)


@frontend_app.route('/')
def home():
    return 'Frontend home'
