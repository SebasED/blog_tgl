from Flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.full_name = data['nombre_completo']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO users(full_name, email, password) VALUES (%(full_name)s,%(email)s,%(password)s)"
        result = connectToMySQL('blog').query_db(query, formulario)
        print(result)
        return result
    
    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('blog').query_db(query, formulario)
        return result

    @classmethod
    def get_name_by_id(cls, formulario):
        query = "SELECT full_name FROM users WHERE id = %(id)s" 
        result = connectToMySQL('blog').query_db(query, formulario)
        return result[0]['full_name']