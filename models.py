from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, ForeignKey


db = SQLAlchemy()


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(120),  nullable=False)
    user = db.Column(db.String(80), ForeignKey('user.username'), nullable=False)
    __table_args__ =( UniqueConstraint('key', 'user'), )

    def __repr__(self):
        return '<User %s><key %s><value %s>' %( self.user, self.key, self.value)


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)


    def __repr__(self):
        return '<name %s><pw %s>' %( self.username, self.password)

