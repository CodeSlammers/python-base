from flask import Flask
from flask_assets import Environment, Bundle


def apply_assets(app: Flask):
    assets = Environment(app)

    js = Bundle(
        'js/html5shiv.min.js',
        'js/respond.min.js'
    )
    css = Bundle(
        'css/sample-app.css'
    )

    assets.register('js_all', js)
    assets.register('css_all', css)
