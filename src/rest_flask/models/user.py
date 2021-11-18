from rest_flask.flask import db
from settings import ENVIRONMENT

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    birth_year = db.Column(db.String(4))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self 

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f"{self.id}"
db.create_all()