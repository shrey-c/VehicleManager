from VM import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(1500), nullable=True)
    password= db.Column(db.String(150), nullable=False)
    
    def __repr__(self):
        return f"User('{self.id}','{self.email_id}')"

class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(1500), nullable=True)
    password= db.Column(db.String(150), nullable=False)
    
    def __repr__(self):
        return f"Admin('{self.id}','{self.email_id}')"


class Car(db.Model):
    __tablename__= 'car'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(1500), nullable=False)
    car_plate = db.Column(db.String(1500), nullable=False)
    car_regNumber=db.Column(db.String(1500), nullable=False)
    date = db.Column(db.String(1500), nullable=False)
    first = db.Column(db.String(1500), nullable=False)
    middle = db.Column(db.String(1500), nullable=False)
    last =db.Column(db.String(1500), nullable=False)
    state = db.Column(db.String(1500), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    r_status = db.Column(db.Integer, unique = False , nullable= False )
    def __repr__(self):
        return f"Car('{self.id}','{self.user_id}','{self.car_plate}','{self.car_regNumber}','{self.date}','{self.first}','{self.middle}','{self.last}','{self.state}','{self.mobile}','{self.r_status}')"

class Request(db.Model):
    __tablename__ = 'request'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, nullable=False)
    user_id =  db.Column(db.Integer, nullable=False)
    r_status = db.Column(db.Integer, unique = False , nullable= False )
    def __repr__(self):
        return f"Request('{self.id},{self.admin_id},{self.user_id},{self.r_status}')"
