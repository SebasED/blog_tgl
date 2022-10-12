from email import message
from typing import List
from flask import render_template, redirect,session, request, jsonify, flash
from Flask_app import app
from Flask_app.models.poem_model import Poem
from Flask_app.models.user_model import User
from Flask_app.models.comment_model import Comment

@app.route('/new_poem')
def new_poem():
    return render_template('new_poem.html')

@app.route('/create_poem', methods=['POST'])
def create_poem():
    print("Entro a create_poem")

    if len(request.form['tittle_poem']) < 1:
        return jsonify(message='Agrega un titulo a tu poema')

    if len(request.form['poem']) < 15:
        return jsonify(message='Escribe tu poema')

    form = {
        "tittle_poem": request.form['tittle_poem'],
        "poem": request.form['poem'],
        "user_id":session['user_id']
    }


    Poem.save_poem(form)
    return jsonify(message='validated')

    # return render_template('bienvenido.html')

def organize_data_for_welcome(poems:List):
    data = []
    for poem in poems:
        form = {
            'id':poem['users_id']
        }
        datum = {
            'tittle_poem':poem['tittle_poem'],
            'poem_author': User.get_name_by_id(form),
            'id_poem': poem['id'],
            'id_creator_poem': poem['users_id'],
        }

        data.append(datum)
    return data

@app.route('/welcome')
def welcome():

    if not session:
        return redirect('/')

    poems = Poem.get_poems()
    data = organize_data_for_welcome(poems)

    user_session = User.get_name_by_id({'id':session['user_id']})
    return render_template('welcome.html',datos=data, user_session=user_session )

@app.route('/show_poem/<int:id_poem>/<int:id_creator_poem>')
def show_poem(id_poem, id_creator_poem):
    if not session:
        return redirect('/')

    poem = Poem.get_poem({'id': id_poem})

    creator = User.get_name_by_id({'id':id_creator_poem})

    #Esta consulta debe devolverme el numbre del usuario que hizo el comentario y el comentario
    comments = Comment.comments_with_user_name_by_id_poem({'id_poem': id_poem})
    datos = {
        'poem': poem['poem'],
        'tittle_poem': poem['tittle_poem'],
        'creator':creator,
        'id_creator':id_creator_poem,
        'id_sesion': session['user_id'],
        'id_poem': id_poem,
        'comments': comments
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
        'creator_id': poem['users_id']
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
    Poem.delete({'id': id_poem})
    return redirect('/welcome')


# dato = {
#             'tittle_poem':poem['tittle_poem'],
#             'poem_author': User.get_name_by_id(form),
#             'id_poem': poem['id'],
#             'id_creator_poem': poem['users_id'],
#         }

@app.route('/get_poem_by_user', methods= ['POST'])
def get_poem_by_user():
    if not session:
        return redirect('/')

    # Get the value for doing the search
    value_to_search = request.form['search']
    return_poems = []

    

    # Validate if the search is for Author
    if request.form['search_option'] == 'Author':
        # Get the authors from the database
        authors = [name['full_name'] for name in User.get_authors()]
        authors_with_poems = []

        # get the authors that match the entered value and save in a list
        for author in authors:
            if value_to_search in author.lower():
                authors_with_poems.append(author)

        if authors_with_poems:
            for author in authors_with_poems:
                return_poems = return_poems + Poem.get_poem_by_author({'author': author})
            #return jsonify(message='validated')
        else:
            flash(f'There are not poems with the user {value_to_search}', 'alert')
            #return jsonify(message=f'There are not poems with the user {value_to_search}')

    # Validate if the search is for Poem
    if request.form['search_option'] == 'Poem':
        # Get the poems tittle from the database
        poems_tittle = [poem['tittle_poem'] for poem in Poem.get_tittle_poems()]
        poems = []

        # get the poems that match the entered value and save in a list
        for poem in poems_tittle:
            if value_to_search in poem.lower():
                poems.append(poem)

        if poems:
            for poem in poems:
                return_poems = return_poems + Poem.get_poem_by_tittle({'tittle': poem})
        else:
            flash(f'There are not poems with the tittle: {value_to_search}', 'alert')
    if request.form['search_option'] == '':
        return redirect('/welcome')

    data = organize_data_for_welcome(return_poems)
    user_session = User.get_name_by_id({'id':session['user_id']})
    return render_template('welcome.html',datos=data, user_session=user_session )


