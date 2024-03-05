from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection


    def find(self, user_id):
        rows = self._connection.execute('SELECT * from users WHERE id =%s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["password"], row["email"])
        


    def create(self, user):
        rows = self._connection.execute('INSERT INTO users(name, password, email) VALUES (%s, %s, %s) RETURNING id', 
                    [user.name, user.password, user.email])
        row = rows[0]
        user.id = row["id"]
        return user