from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, InputRequired

class Signupform(FlaskForm):
    email = EmailField('Email', validators = [InputRequired()])
    username = StringField('username', validators = [InputRequired()])
    password = PasswordField('password', validators = [InputRequired()])
    confirm_password = PasswordField('confirm password', validators = [InputRequired(), EqualTo("password")])
    submit = SubmitField()