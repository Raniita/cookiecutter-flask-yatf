from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(FlaskForm):
    """ User sign-up Form """

    name = StringField(
        'Name',
        validators=[DataRequired()]
    )

    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )

    confirm = PasswordField(
        'Confirm your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Password must match.')
        ]
    )

    website = StringField(
        'Website',
        validators=[Optional()]
    )

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """ User Log-in Form. """

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    submit = SubmitField('Log In')

    
class ChangePasswordForm(FlaskForm):
    """ User change password """

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )

    confirm = PasswordField(
        'Confirm your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Password must match.')
        ]
    )

    new_password = PasswordField(
        'New Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )

    confirm_new = PasswordField(
        'Confirm your Password',
        validators=[
            DataRequired(),
            EqualTo('new_password', message='Password must match.')
        ]
    )

    submit = SubmitField('Change actual user password')
