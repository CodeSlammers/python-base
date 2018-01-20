class CrudExtension(object):
    @property
    def db(self):
        if not hasattr(self, '_db'):
            self._db = None
        if self._db is None:
            from . import get_db
            self._db = get_db()
        return self._db

    def save(self):
        if self.id is None:
            self.db.session.add(self)
        return self.db.session.commit()

    def destroy(self):
        self.db.session.delete(self)
        return self.db.session.commit()
