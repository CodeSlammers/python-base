from flask import Flask
from database import register_db
from flask_bootstrap import Bootstrap
from nav import nav
from bundle import apply_assets

app = Flask(__name__)
app.config.from_object('config.DevConfig')
register_db(app)
nav.init_app(app)
Bootstrap(app)
apply_assets(app)

from api import api_app
from frontend import frontend_app
app.register_blueprint(api_app, url_prefix='/api')
app.register_blueprint(frontend_app, url_prefix='/app')

@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run()
