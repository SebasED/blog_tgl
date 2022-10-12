from Flask_app.config.mysqlconnection import connectToMySQL
from flask import jsonify

class Poem:

    def __init__(self,data):
        self.id = data['id'],
        self.title_poem = data['tittle_poem'],
        self.poem = data['poem'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.user_id = data['user_id']

    @classmethod
    def save_poem(cls,form):
        """Create and save a poem into the database

        Args:
            form (dict): data for saving in database

        Returns:
            int: poem id
        """
        query = "INSERT INTO poems(tittle_poem, poem, users_id) VALUES (%(tittle_poem)s,%(poem)s,%(user_id)s)"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def get_poems(cls):
        """to get the poems from the database

        Returns:
            list: list of poems
        """
        query = "SELECT tittle_poem, users_id, id FROM poems "
        result = connectToMySQL('blog').query_db(query)
        return result

    @classmethod
    def get_poem(cls, form):
        """to get a poem from the database

        Args:
            form (dict): poem id

        Returns:
            dict: poem data
        """
        query = "SELECT tittle_poem, users_id, poem FROM poems WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result[0]

    @classmethod
    def update_poem(cls, form):
        """to update a poem in the database

        Args:
            form (dict): poem data

        Returns:
            int: poem id
        """
        query = "UPDATE poems SET tittle_poem = %(tittle_poem)s, poem = %(poem)s  where id = %(id)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def delete(cls, form):
        """to delete a poem from the database

        Args:
            form (dict): poem id
        Returns:
            int: poem id
        """
        query = "DELETE FROM poems WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def get_tittle_poems(cls):
        query = "SELECT tittle_poem FROM poems"
        result = connectToMySQL('blog').query_db(query)
        return result

    @classmethod
    def get_poem_by_author(cls, form):
        #SELECT * FROM blog.poems Where users_id = (select id from blog.users where full_name='Sebas Estrada');
        query = "SELECT tittle_poem, users_id, id FROM poems WHERE users_id = (SELECT id FROM users WHERE fulL_name = %(author)s)"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def get_poem_by_tittle(cls, form):
        query = "SELECT tittle_poem, users_id, id FROM poems WHERE tittle_poem = %(tittle)s"
        result = connectToMySQL('blog').query_db(query, form)
        print("---------------------------")
        print(result)
        return result
