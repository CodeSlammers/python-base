from flask import Flask
from database import register_db, get_db

app = Flask(__name__)
app.config.from_object('config.DevConfig')
register_db(app)

from api import api_app
from frontend import frontend_app
app.register_blueprint(api_app, url_prefix='/api')
app.register_blueprint(frontend_app, url_prefix='/app')

@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
