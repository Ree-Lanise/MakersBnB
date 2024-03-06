class Booking:
    def __init__(self, id, property_id, owner_id, guest_id, starting_date, end_date):
        self.id = id
        self.property_id = property_id
        self.owner_id = owner_id
        self.guest_id = guest_id
        self.starting_date = starting_date
        self.end_date = end_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Booking({self.id}, {self.property_id}, {self.owner_id}, {self.guest_id}, {self.starting_date}, {self.end_date})'