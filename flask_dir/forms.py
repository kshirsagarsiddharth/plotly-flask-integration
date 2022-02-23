from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_dir.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min = 2, max = 20)
    ])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')
    # validators if the username and email already exists
    def validate_username(self, username):
        # if the username already exists throw validation error 
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('The Username is taken')
    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('The Email is taken')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators = [
        DataRequired(),Length(min = 2, max = 20)
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_image = FileField('Upload Profile Pic', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('The username is taken. Please choose another username')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('The email is taken. Perhaps you alreadu have an account')
    
    
    