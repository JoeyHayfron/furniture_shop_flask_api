from datetime import datetime

from sqlalchemy import inspect
from sqlalchemy.orm import validates

from .. import db


class Product(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    product_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String, nullable=False)
    type = db.Column(db.String(255), nullable=False)

    @validates('product_name')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    def toDict(self):
        print(f"LETS SEE {inspect(self).mapper.column_attrs}")
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return '<Product %r>' % self.product_name
