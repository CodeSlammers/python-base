from flask import Blueprint
from database.models import Counter
api_app = Blueprint('api', __name__)


@api_app.route('/')
def home():
    return 'API home'


@api_app.route('/count')
def increment_counter():
    count = Counter.query.first()
    if count is None:
        count = Counter()
        count.value = 0

    count.value += 1
    count.save()

    return 'Count is {}'.format(count.value)
