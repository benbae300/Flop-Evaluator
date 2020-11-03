"""Signup & login forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Optional


class SignupForm(FlaskForm):
    """User Signup Form."""
    name = StringField('Create Username:',
                       validators=[DataRequired()])
    password = PasswordField('Create Password:',
                             validators=[DataRequired(),
                                         Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Confirm Password:',
                            validators=[DataRequired(),
                                        EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Get Started Now!')


class LoginForm(FlaskForm):
    """User Login Form."""
    name = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Log In!')