from lib.user import User
import hashlib

class UserRepository:

    def __init__(self, connection):
        self._connection = connection


    def find(self, user_id):
        rows = self._connection.execute('SELECT * from users WHERE id =%s', [user_id])
        if rows == []: 
            return False
        row = rows[0]
        return User(row["id"], row["name"], row["password"], row["email"])
        
    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        if rows == []: 
            return False
        row = rows[0]
        return User(row["id"], row["name"], row["password"], row["email"])
        

    def create(self, user):
        rows = self._connection.execute('INSERT INTO users(name, password, email) VALUES (%s, %s, %s) RETURNING id', 
                    [user.name, user.password, user.email])
        row = rows[0]
        user.id = row["id"]
        return user

    def check_password(self, email, password_attempt):
        # check whether there is a user in the database with the given email and 
        # a matching password using a SELECT statement
        print(email, password_attempt)
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', 
            [email, password_attempt])
        print(rows)
        return len(rows) > 0
