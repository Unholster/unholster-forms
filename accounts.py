from db import db
from forms import form

class account(dict):
    def form(self, form_name):
        for f in self.get('forms', []):
            if f['name'] == form_name:
                return form(f)
    
    def submits(self):
        return db['ac_{_id}_submits'.format(**self)]


def find_one(spec):
    data = db.accounts.find_one(
        spec
    )
    if data:
        return account(data)


db.accounts.ensure_index( [('name',1)], cache_for=3600, unique=True)
db.accounts.ensure_index( [('_id',1), ('forms.name',1)], cache_for=3600, unique=True)
db.accounts.ensure_index( [('forms.referers',1)], cache_for=3600, unique=True)