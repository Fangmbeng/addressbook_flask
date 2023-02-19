from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import Signupform

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(username, email, password)
        if username == 'Brandon':
            flash('The user already exist')
            return redirect(url_for('signup'))

        flash('Thank you for signing up !')
        return redirect(url_for('index'))
    
    return render_template('signup.html', form = form)