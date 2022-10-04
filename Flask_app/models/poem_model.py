from Flask_app.config.mysqlconnection import connectToMySQL
from flask import jsonify

class Poema:

    def __init__(self,data):
        self.id = data['id'],
        self.title_poem = data['title_poem'],
        self.poem = data['poem'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.user_id = data['user_id']


    @classmethod
    def save_poem(cls,formulario):
        query = "INSERT INTO poems(title_poem, poem, users_id) VALUES (%(title_poem)s,%(poem)s,%(user_id)s)"
        result = connectToMySQL('blog').query_db(query, formulario)
        return result

    @classmethod
    def get_poems(cls):
        query = "SELECT title_poem, users_id, id FROM poems "
        result = connectToMySQL('blog').query_db(query)
        return result
    
    @classmethod
    def get_poem(cls, formulario):
        query = "SELECT title_poem, users_id, poem FROM poems WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, formulario)
        return result[0]
    
    @classmethod
    def update_poem(cls, formulario):
        print()
        query = "UPDATE poems SET title_poem = %(title_poem)s, poem = %(poem)s  where id = %(id)s"
        result = connectToMySQL('blog').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM poems WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, formulario)
        return result

    



