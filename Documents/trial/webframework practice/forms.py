"""wt forms we are importing the flaskform"""
from flask_wtf import FlaskForm

"""importing the stringfield"""
from wtforms import StringField, PasswordField, SubmitField, BooleanField

"""importing validator """
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Registrationform(FlaskForm):
    #creating a variable username
    #validators - restrictions for username
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    #email field
    email = StringField('Email', validators=[DataRequired(), Email()])

    #passwordfield
    password = PasswordField('Password', validators=[DataRequired()])

    #password confirmation
    confirm_password =     password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])

    #subnmitField
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])

    remember = BooleanField('Remember me')

    submit = SubmitField('Log in')
