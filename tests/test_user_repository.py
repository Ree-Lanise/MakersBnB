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
    repo = UserRepository(db_connection)
    
    # we need to hash a password for the function to work 
    password = '12345'
    binary_password_attempt = password.encode("utf-8")
    hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
    
    # we pass the hashed password into a create method to create a user with this password 
    repo.create(User(None, 'John', f'{hashed_password_attempt}', 'John@outlook.com'))
    
    # we use the check password function with the original password attempt
    result = repo.check_password('John@outlook.com', '12345')
    
    # we assert the result returns true 
    assert result == True


# # NOW WE DO THE SAME BUT TRY GET A FALSE RESULT

def test_check_password_false(db_connection):
    db_connection.seed("seeds/Users.sql")
    repo = UserRepository(db_connection)
    
    # we need to hash a password for the function to work 
    password = '12345'
    binary_password_attempt = password.encode("utf-8")
    hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
    
    # we pass the hashed password into a create method to create a user with this password 
    repo.create(User(None, 'John', f'{hashed_password_attempt}', 'John@outlook.com'))
    
    # we use the check password function with the original password attempt
    result = repo.check_password('John@outlook.com', 'FAKE PASSWORD')
    
    # we assert the result returns FALSE
    assert result == False