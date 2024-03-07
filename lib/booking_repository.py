from lib.booking import Booking
class BookingRepository():
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(row['id'], row['property_id'], row['owner_id'], row['guest_id'], row['starting_date'], row['end_date'], row['status'], row['name'])
            bookings.append(booking)
        return bookings
    
    def find(self,id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id=%s",[id])
        row = rows[0]
        return Booking(row['id'], row['property_id'], row['owner_id'], row['guest_id'], row['starting_date'], row['end_date'], row['status'], row['name'])
    
    def create(self, booking):
        rows = self._connection.execute("INSERT INTO bookings(property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES (%s,%s,%s,%s,%s, %s, %s) RETURNING id",
                                        [booking.property_id, booking.owner_id, booking.guest_id, booking.starting_date, booking.end_date, "pending", booking.name])
        row = rows[0]
        booking.id = row["id"]
        return booking
    
    def update(self, id):
        rows = self._connection.execute(
            "UPDATE bookings SET status = 'Confirmed' WHERE id = %s",[id])
        
    def delete(self, id):
        self._connection.execute(
            "DELETE FROM bookings WHERE id = %s",[id])
        
    def all_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id = %s", [id])
        bookings = []
        for row in rows:
            booking = Booking(row['id'], row['property_id'], row['owner_id'], row['guest_id'], row['starting_date'], row['end_date'], row['status'], row['name'])
            bookings.append(booking)
        return bookings
        
        
        
    #update method "SELECT * FROM bookings WHERE id=%s",[ownwer_id]