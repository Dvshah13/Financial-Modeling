from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from models import *
from flask.ext.bcrypt import Bcrypt
from flask.ext.csrf import csrf
import logging

app = Flask(__name__)
app.config.from_object('settings')
bcrypt = Bcrypt(app)
csrf(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/new_user', methods=['GET', 'POST'])
def create_user():


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            this_user = User.objects.get(email=request.form['username'])
            if request.form['username'] != this_user.email:
                error = 'Invalid username'
            elif bcrypt.check_password_hash(this_user.password, request.form['password']) == False:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                session['email_user'] = {'email': this_user.email}
                session['first_name_user'] = {'first_name':this_user.first_name}
                flash('You were logged in')
                return render_template('dashboard.html', first_name=session.get('first_name_user'), email=session.get('email_user'))
        except:
            flash('User does not exist')
    return render_template('new_user.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
