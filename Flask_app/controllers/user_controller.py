from Flask_app import app
from Flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect,session, request, jsonify
from Flask_app.models.user_model import User
import re
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/user_registration', methods=['POST'])
def user_registration():

    if len(request.form['full_name']) < 5:
        return  jsonify(message='Type your fullname')

    if not EMAIL_REGEX.match(request.form['email']):
        return jsonify(message='Invalid email')


    query = "SELECT * FROM users WHERE email = %(email)s"
    results = connectToMySQL('blog').query_db(query, request.form)
    if len(results) >= 1:
        return jsonify(message='The email already exists')

    if len(request.form['password']) < 6:
        return jsonify(message='The password must contain at least 6 characters')

    if request.form['password'] != request.form['confirm_password']:
        return jsonify(message='Passwords do not match')


    secret = bcrypt.generate_password_hash(request.form['password'])

    formulario = {
        "full_name": request.form['full_name'],
        "email": request.form['email'],
        "password":secret
    }

    User.save(formulario)

    return jsonify(message='validated')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/session_start', methods=['POST'])
def session_start():

    if len(request.form["email"]) < 1:
        return jsonify(message="Email required")

    user = User.get_by_email(request.form)
    if not user:
        return jsonify(message='Email not registered')

    if len(request.form['password']) < 1:
        return jsonify(message="Type your password")

    if not bcrypt.check_password_hash(user[0]["password"],request.form["password"]):
        return jsonify(message="wrong password")

    session['user_id'] = user[0]['id']

    return jsonify(message='validated')

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/')
