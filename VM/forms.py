from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required, NumberRange, ValidationError
from SH.models import User, Emails , Conversation

class RegisterForm(FlaskForm):
    email = StringField('Name', validators=[DataRequired(), Length(max=120) ,Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Proceed')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')

class AdminRegistrationForm(FlaskForm):
    email = StringField('Name', validators=[DataRequired(), Length(max=120) ,Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Proceed')

    def validate_email(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError('Tha email is taken. Please choose a different one.')


class Car_registration(FlaskForm):
    user_id = IntegerField("ID no.", validators=[DataRequired()])
    car_plate = StringField("Car Plate ID", validators=[DataRequired()])
    car_regNumber=IntegerField("Car Registration Number",  validators=[DataRequired()])
    date = DateField("Date of Registration",  validators=[DataRequired()])
    first = StringField("First Name",  validators=[DataRequired()])
    middle = StringField("Middle Name",  validators=[DataRequired()])
    last =StringField("Last Name",  validators=[DataRequired()])
    state = StringField("Enter State",  validators=[DataRequired()])
    mobile = IntegerField("Enter Mobile No.",  validators=[DataRequired()])
    submit = SubmitField('Login')



class RequestForm(FlaskForm):
    invite_status = RadioField('You have an invite!', choices=[('1','Accept'),('0','Decline')])
    submit=SubmitField('Submit')

