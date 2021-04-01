
from app import db,bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

#用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(32))
    password = db.Column(db.String(128))

    def set_password(self, p):
        self.password = generate_password_hash(p)

    def check_password(self, p):
        ispass = check_password_hash(self.password, p)
        return ispass

db.create_all()