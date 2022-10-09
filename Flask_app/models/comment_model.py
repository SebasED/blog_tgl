from Flask_app.config.mysqlconnection import connectToMySQL

class Comment:

    def __init__(self,data):
        self.id = data['id'],
        self.comment = data['comment'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.user_id = data['user_id'],
        self.poem_id = data['poem_id']

    @classmethod
    def save_comment(cls, form):
        query = "INSERT INTO comments(comment, poems_id, users_id) VALUES (%(comment)s,%(id_poem)s,%(id_user)s)"
        result = connectToMySQL('blog').query_db(query, form)
        print(result)
        return result
    
    @classmethod
    def get_comments_by_id_poem(cls, form):
        query = "SELECT * FROM comments WHERE poems_id = %(id_poem)s"
        result = connectToMySQL('blog').query_db(query, form)
        print("----------------------")
        print(result)
        return result