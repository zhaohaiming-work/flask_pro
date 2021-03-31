
from app import db

#用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(32))
    password = db.Column(db.String(32))

db.create_all()