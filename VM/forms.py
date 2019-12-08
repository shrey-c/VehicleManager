from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, NumberRange, ValidationError
from VM.models import User, Admin, Car, Request

class RegisterForm(FlaskForm):
    email_id = StringField('Name', validators=[DataRequired(), Length(max=120) ,Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Proceed')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')

class AdminLoginForm(FlaskForm):
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')

class AdminRegisterForm(FlaskForm):
    email_id = StringField('Name', validators=[DataRequired(), Length(max=120) ,Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Proceed')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')


class CarRegistration(FlaskForm):
    car_plate = StringField("Car Plate ID", validators=[DataRequired()])
    car_regNumber=StringField("Car Registration Number",  validators=[DataRequired()])
    date = StringField("Date of Registration",  validators=[DataRequired()])
    first = StringField("First Name",  validators=[DataRequired()])
    middle = StringField("Middle Name",  validators=[DataRequired()])
    last =StringField("Last Name",  validators=[DataRequired()])
    state = StringField("Enter State",  validators=[DataRequired()])
    mobile = IntegerField("Enter Mobile No.",  validators=[DataRequired()])
    submit = SubmitField('Submit')



class RequestForm(FlaskForm):
    invite_status = RadioField('You have an invite!', choices=[('1','Accept'),('0','Decline')])
    submit=SubmitField('Submit')

