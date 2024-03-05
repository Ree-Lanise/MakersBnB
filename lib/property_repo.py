from lib.property import Property

class PropertyRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self): 
        rows = self._connection.execute("SELECT * FROM properties;")
        properties = []
        for row in rows: 
            property = Property(row['id'], row['name'], row['description'], row['price'], row['user_id'], row['available_start'], row['available_end'])
            properties.append(property)
        return properties
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM properties WHERE id = %s", [id])
        row = rows[0]
        return Property(row["id"], row["name"], row["description"], row["price"], row["user_id"], row['available_start'], row['available_end'])
    
    
    def create_space(self, property_instance):
        rows = self._connection.execute(
        "INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id", 
        [property_instance.name, property_instance.description, property_instance.price, property_instance.user_id, property_instance.aval_start, property_instance.aval_end])
        row = rows[0]
        property_instance.id = row["id"]
        return property_instance
    
    
    
        
        
        
        
        


