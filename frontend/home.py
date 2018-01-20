from flask import render_template
from .app import frontend_app


@frontend_app.route('/')
def index():
    return render_template('index.html')

