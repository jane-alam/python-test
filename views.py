from app import app
from models import Users
from forms import LoginForm
from flask import render_template

@app.route('/')
def homepage():
    return "Hello World"

@app.route('/login')
def Login():
    form = LoginForm()
    return render_template('login.html', form = form)