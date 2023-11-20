from datetime import datetime
from random import choices
from string import ascii_letters, digits

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('index_view', short_id=self.short, _external=True)
        )

    def get_unique_short_id():
        while True:
            short_id = ''.join(choices(ascii_letters + digits, k=6))
            if not URLMap.query.filter_by(short=short_id).first():
                return short_id

    def is_valid_short_id(short_id):
        if len(short_id) > 16:
            return False
        for value in short_id:
            if value not in ascii_letters and value not in digits:
                return False
        return True
