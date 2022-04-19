from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import State

bcrypt = Bcrypt(app)

@app.route('/')
def registration():
    return redirect('/dashboard')
    #return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not user.validate(request.form):
        return redirect('/')
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['User_id'] = User.save(data)
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # see if the User name provided exists in the database
    data = { "email" : request.form["login-email"] }
    User_in_db = User.get_User_by_email(data)
    # User is not registered in the db
    if not User_in_db:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(User_in_db.password, request.form['login-password']):
        # if we get False after checking the password
        flash("Invalid Email/Password","login")
        return redirect('/')
    # if the passwords matched, we set the User_id into session
    session['User_id'] = User_in_db.id
    session['firstname'] = User_in_db.first_name
    session['lastname'] = User_in_db.last_name

    return redirect('/dashboard')

@app.route('/dashboard')
def home():
    # whr 04/19/2022 - skipping the login stuff right now
    session['User_id'] = 1
    session['firstname'] = 'William'
    session['lastname'] = 'Rohde'

    data = {
        'id': session['User_id']
    }
    return render_template('dashboard.html',states = State.state.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')