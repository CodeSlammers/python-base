from .. import get_db, CrudExtension
db = get_db()


class Counter(db.Model, CrudExtension):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)

    def __repr__(self):
        return '<Count: {}>'.format(self.value)

