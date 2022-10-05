from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
from Flask_app.models.poem_model import Poem
from Flask_app.models.user_model import User

@app.route('/welcome')
def welcome():

    if not session:
        return redirect('/')
    
    datos = []

    
    poemas = Poem.get_poems()
    for poema in poemas:
        formulario = {
            'id':poema['usuario_id']
        }
        dato = {
            'titulo_poema':poema['titulo_poema'], 
            'autor': User.get_name_by_id(formulario),
            'id_poema': poema['id'],
            'id_creador_poema': poema['usuario_id']
        }

        datos.append(dato)
    
    autor = User.get_name_by_id({'id':session['usuario_id']})
    

    return render_template('welcome.html',datos=datos, autor= autor )