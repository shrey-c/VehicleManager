from VM import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1500), nullable=True)
    password= db.Column(db.String(150), nullable=False)
    licence= db.Column(db.String(120))
    
    def __repr__(self):
        return f"User('{self.username}','{self.licence}','{self.id}')"

class Admin(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(1500), nullable=True)
    password= db.Column(db.String(150), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.licence}','{self.id}')"


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(1500), nullable=False)
    license = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    registration = db.Column(db.Integer, db.ForeignKey('conversing.id'))
    r_status = db.Column(db.Integer, unique = False , nullable= False )
    def __repr__(self):
        return f"Conversation('{self.text}','{self.time}','{self.conversing_id}', '{self.sender_id}')"


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, nullable=False)
    user_id =  db.Column(db.Integer, nullable=False)
    r_status = db.Column(db.Integer, unique = False , nullable= False )
    def __repr__(self):
        return f"Conversation('{self.text}','{self.time}','{self.conversing_id}', '{self.sender_id}')"



