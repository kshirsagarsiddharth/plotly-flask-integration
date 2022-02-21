
from flask import Flask, render_template, flash, redirect, url_for
from flask_dir import flask_app, app  
from bs4 import BeautifulSoup
from flask_dir.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from flask_dir import bcrypt, db
from flask_dir.models import User



@flask_app.route('/')
@flask_app.route('/home')
def home():
    return render_template('home.html')

@flask_app.route('/dashapp', methods=['GET', 'POST'])
def dashapp():
    soup = BeautifulSoup(app.index(), 'html.parser')
    footer = soup.footer
    return render_template('dash1.html', title='test', footer=footer)


@flask_app.route('/register', methods = ['GET','POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account Successfully Created You are now a member ", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'register', form = form)

@flask_app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            redirect(url_for('home'))
        else:
            flash("Please check email and password")

    return render_template('login.html', title = 'Login', form = form)    

@login_required
@flask_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
   
