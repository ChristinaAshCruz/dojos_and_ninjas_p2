from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self, db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        # self.dojos_id = db_data['dojos_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save_ninja(cls, db_data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s, NOW(), NOW());"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,db_data)
        return result

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, id )
        print(result)
        return (cls(result[0]))

    @classmethod
    def update(cls, db_data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s and dojos_id = %(dojos_id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query, db_data )
        return result