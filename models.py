from db import db

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return self.name