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
        """Create and save a comment into the database

        Args:
            form (dict): data for saving in database

        Returns:
            int: comment id
        """
        query = "INSERT INTO comments(comment, poems_id, users_id) VALUES (%(comment)s,%(id_poem)s,%(id_user)s)"
        result = connectToMySQL('blog').query_db(query, form)
        print(result)
        return result

    @classmethod
    def comments_with_user_name_by_id_poem(cls, form):
        """to get the comments from the database

        Args:
            form (dict): poem id

        Returns:
            list: list of comments
        """
        # SELECT c.*, u.full_name FROM blog.comments c left join blog.users u On c.users_id = u.id where c.poems_id = 3;
        query = "SELECT c.*, u.full_name FROM comments c left join users u On c.users_id = u.id WHERE poems_id = %(id_poem)s"
        result = connectToMySQL('blog').query_db(query, form)
        print("--------------------------------------------")
        print(result)
        return result

    @classmethod
    def get_poem_by_comment_id(cls, form):
        query = "SELECT * FROM poems WHERE id = (select poems_id from comments where id = %(id)s)"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def delete(cls, form):
        """to delete a comment from the database

        Args:
            form (dict): comment id

        Returns:
            int: comment id deleted
        """
        query = "DELETE FROM comments WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result