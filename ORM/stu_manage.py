
from app import db

#用户
class Stu_manage(db.Model):
    __tablename__ = 'stu_manage'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    stu_name = db.Column(db.String(32),nullable=False)
    class_code = db.Column(db.Enum('1','2','3','4','5'),server_default='1')
    height=db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum('男','女'),server_default='男')
    weight= db.Column(db.Integer)
    

db.create_all()