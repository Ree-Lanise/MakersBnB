from lib.user_repository import UserRepository
from lib.user import User
import hashlib

'''
Test connection between conftest.py and lib
'''

def test_find(db_connection):
    db_connection.seed("seeds/Users.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')


def test_create(db_connection):
    db_connection.seed("seeds/Users.sql")
    repository = UserRepository(db_connection)


    user = repository.create(User(None, 'John', '12345', 'John@outlook.com'))
    result = repository.find(user.id)
    assert result == user



def test_check_password(db_connection):
    db_connection.seed("seeds/Users.sql")
    
    # we have to create a hashed password because the seed file has 
    # a normal password as a string 
    
    password = 'P*ssword'
    binary_password_attempt = password.encode("utf-8")
    hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
    
    # we initialise a new user instance with the hashed password 
    
    user = User(2, 'Aakash', hashed_password_attempt, 'Aakash@outllok.com')
    
    # we init a repo and create a user with a hashed password
    
    repo = UserRepository(db_connection) 
    repo.create(user)
    
    # we use check password to check the details and assert it returns true 
    
    result = repo.check_password(user.email, user.password)
    assert result == True
    