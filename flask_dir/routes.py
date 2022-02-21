
from flask import Flask, render_template, flash, redirect, url_for
from flask_dir import flask_app, app  
from bs4 import BeautifulSoup
from flask_dir.forms import RegistrationForm, LoginForm



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
    form = RegistrationForm()
    return render_template('register.html', title = 'register', form = form)

@flask_app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)    
   
