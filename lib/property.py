class Property:
    def __init__(self, id, name, description, price, user_id, aval_start, aval_end):
        self.id = id
        self.name = name
        self.description = description
        self.price = price 
        self.user_id = user_id #possibly user_id
        self.aval_start = aval_start
        self.aval_end = aval_end
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.name}\n {self.description}\n £{self.price}\n Owner: {self.user_id} {self.aval_start}\n {self.aval_end}\n "
        
        
        