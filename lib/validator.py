import re 
class Validator():
    space_error = "can't have spaces"
    password_error = """password invalid - must be seven 
                            characters long and contain one special 
                            character: ! @ £ $ % ^ & *
                            """
    email_error = "invalid email address"
    def check_spaces(username, password, email):
        if " " in username  or " " in password or " " in email:
            return True 
        else: 
            return False 
    
    def check_password_invalid(password):
        for char in password: 
            if char in "!@£$%^&*" and len(password) > 7: 
                return False 
        else: 
            return True 
                
    def check_email(email):
        pattern = re.compile("[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
        return pattern.match(email)

