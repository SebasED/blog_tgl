from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
from Flask_app.models.poem_model import Poem
from Flask_app.models.user_model import User

@app.route('/new_poem')
def new_poem():
    return render_template('new_poem.html')

@app.route('/create_poem', methods=['POST'])
def create_poem():
    
    
    if len(request.form['tittle_poem']) < 1:
        return jsonify(message='Agrega un titulo a tu poema')

    if len(request.form['poem']) < 30:
        return jsonify(message='Escribe tu poema')

    form = {
        "tittle_poem": request.form['tittle_poem'],
        "poem": request.form['poem'],
        "user_id":session['user_id']
    }


    Poem.save_poem(form)
    return jsonify(message='Validated')

    # return render_template('bienvenido.html')



@app.route('/welcome')
def welcome():

    if not session:
        return redirect('/')
    
    datos = []

    
    poems = Poem.get_poems()
    for poem in poems:
        form = {
            'id':poem['user_id']
        }
        dato = {
            'tittle_poem':poem['tittle_poem'], 
            'author': User.get_name_by_id(form),
            'id_poem': poem['id'],
            'id_creator_poem': poem['user_id']
        }

        datos.append(dato)
    
    author = User.get_name_by_id({'id':session['user_id']})
    

    return render_template('welcome.html',datos=datos, author= author )

@app.route('/show_poem/<int:id_poem>/<int:id_creator_poem>')
def show_poem(id_poem, id_creator_poem):
    if not session:
        return redirect('/')
    
    form = {'id': id_poem}
    
    
    poem = Poem.get_poem(form)
    
    creator = User.get_name_by_id({'id':id_creator_poem})
    
    
    datos = {
        'poem': poem['poem'],
        'tittle_poem': poem['tittle_poem'],
        'creator':creator,
        'id_creator':id_creator_poem, 
        'id_sesion': session['user_id'],
        'id_poem': id_poem
    }

    return render_template('poems.html', datos=datos)



@app.route('/update/poem/<int:id_poem>')
def update_poem(id_poem):
    if not session:
        return redirect('/')

    form = {'id': id_poem}
    
    poem = Poem.get_poem(form)
    
    datos = {
        'poem': poem['poem'],
        'tittle_poem': poem['tittle_poem'],
        'poem_id': id_poem,
        'creator_id': poem['user_id']
    }

    return render_template('update.html', datos = datos )

@app.route('/modify_poem', methods= ['POST'])
def modify_poem():
    

    form = {
        'tittle_poem': request.form['tittle_poem'],
        'poem': request.form['poem'],
        'id': request.form['poem_id']
    }

    id_poem = request.form['poem_id']
    id_creator = request.form['creator_id']

    Poem.update_poem(form)
    
    return redirect(f'/show_poem/{id_poem}/{id_creator}')


@app.route('/delete/<int:id_poem>')
def delete(id_poem):
    form = {
            'id': id_poem
        }
    
    Poem.delete(form)
    return redirect('/welcome')
