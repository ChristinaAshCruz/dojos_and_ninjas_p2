from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        return results

        for one_dojo in results:
            dojos.append( cls(one_dojo) )
        return dojos

    @classmethod
    def save(cls, db_data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,db_data)
        return result

    @classmethod
    def get_one( cls, db_data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, db_data)
        print(results)
        dojo = cls(results[0])
        for row in results: 
            one_ninja_data = {
            'id': row['ninjas.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'age': row['age'],
            'created_at': row['ninjas.created_at'],
            'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(one_ninja_data) )
        return dojo