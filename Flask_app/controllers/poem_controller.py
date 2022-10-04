from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
#from Flask_app.models.poemas import Poema
#from Flask_app.models.usuarios import User

@app.route('/bienvenido')
def bienvenido():

    if not session:
        return redirect('/')
    
    datos = []

    
    poemas = Poema.obtener_poemas()
    for poema in poemas:
        formulario = {
            'id':poema['usuario_id']
        }
        dato = {
            'titulo_poema':poema['titulo_poema'], 
            'autor': Usuario.get_name_by_id(formulario),
            'id_poema': poema['id'],
            'id_creador_poema': poema['usuario_id']
        }

        datos.append(dato)
    
    autor = Usuario.get_name_by_id({'id':session['usuario_id']})
    

    return render_template('bienvenido.html',datos=datos, autor= autor )