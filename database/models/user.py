from .. import get_db, CrudExtension
db = get_db()


class User(db.Model, CrudExtension):
    id = db.Column(db.Integer, primary_key=True)
    pass
