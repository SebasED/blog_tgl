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
def registro():

    if len(request.form['nombre_completo']) < 5:
        return  jsonify(message='Escribe tu nombre completo')

    if not EMAIL_REGEX.match(request.form['email']):
        return jsonify(message='Email invalido')


    query = "SELECT * FROM users WHERE email = %(email)s"
    results = connectToMySQL('blog').query_db(query, request.form)
    if len(results) >= 1:
        return jsonify(message='El email ya existe')

    if len(request.form['contraseña']) < 6:
        return jsonify(message='La contraseña debe contener al menos 6 caracteres')

    if request.form['contraseña'] != request.form['confirma_contraseña']:
        return jsonify(message='Las contraseñas no coinciden')


    secret = bcrypt.generate_password_hash(request.form['contraseña'])

    formulario = {
        "full_name": request.form['nombre_completo'],
        "email": request.form['email'],
        "password":secret
    }

    User.save(formulario)

    return jsonify(message='validado')

@app.route('/inicia_sesion')
def inicia_sesion():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    if len(request.form["email"]) < 1:
        return jsonify(message="Email requerido")

    user = User.get_by_email(request.form)
    if not user:
        return jsonify(message='Email no registrado')

    if len(request.form['password']) < 1:
        return jsonify(message="Escribe tu contraseña")

    if not bcrypt.check_password_hash(user[0]["password"],request.form["password"]):
        return jsonify(message="Contraseña incorrecta")

    session['usuario_id'] = user[0]['id']

    return jsonify(message='validado')
