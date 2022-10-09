from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
import Flask_app
from Flask_app.models.comment_model import Comment
from Flask_app.models.poem_model import Poem

@app.route('/new_comment/<int:id_poem>/<int:id_user_session>', methods= ['POST'])
def new_comment(id_poem, id_user_session):
    if not session:
        return redirect('/')

    form = {
        "comment": request.form['comment'],
        "id_poem": id_poem,
        "id_user": id_user_session
    }

    Comment.save_comment(form)
    id_creator = Poem.get_poem({'id':id_poem})['users_id']

    return redirect(f'/show_poem/{id_poem}/{id_creator}')

