from Flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['full_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,form):
        query = "INSERT INTO users(full_name, email, password) VALUES (%(full_name)s,%(email)s,%(password)s)"
        result = connectToMySQL('blog').query_db(query, form)
        print(result)
        return result
    
    @classmethod
    def get_by_email(cls, form):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result

    @classmethod
    def get_name_by_id(cls, form):
        query = "SELECT full_name FROM users WHERE id = %(id)s"
        result = connectToMySQL('blog').query_db(query, form)
        return result[0]['full_name']