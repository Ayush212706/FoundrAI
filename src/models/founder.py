from src.models.database import db


class Founder(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    age = db.Column(db.Integer)

    education = db.Column(db.String(100))

    occupation = db.Column(db.String(100))

    score = db.Column(db.Integer)