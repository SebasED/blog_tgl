from flask import render_template, redirect,session, request, jsonify
from Flask_app import app
import Flask_app
from Flask_app.models.comment_model import Comment
from Flask_app.models.poem_model import Poem

@app.route('/new_comment/<int:id_poem>/<int:id_user_session>', methods= ['POST'])
def new_comment(id_poem, id_user_session):
    """to create a new comment

    Args:
        id_poem (int): id from poem that will be commented
        id_user_session (int): id from user that makes de comment

    Returns:
        redirect: show the poem where made the comment
    """
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

@app.route('/delete_comment/<int:id_comment>')
def delete_comment(id_comment):
    """to delete a comment 

    Args:
        id_comment (int): id from comment that will be deleted

    Returns:
        redirect: redirect to show poems without deleted comment
    """
    print("Ingrese al metodo de eliminar comment")
    poem = Comment.get_poem_by_comment_id({'id': id_comment})
    id_poem = poem[0]['id']
    id_creator = poem[0]['users_id']
    Comment.delete({'id': id_comment})
    return redirect(f'/show_poem/{id_poem}/{id_creator}')
