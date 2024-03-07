from lib.booking_repository import BookingRepository
from lib.booking import Booking
import datetime

def test_all(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    bookings = repo.all()
    assert bookings == [Booking(1, 1, 5, 1, datetime.date(2023, 3, 1), datetime.date(2023,3,5), "pending",'Chestnut Eco Lodge Woodland Escape'),
                        Booking(2, 2, 4, 2, datetime.date(2023,3,5), datetime.date(2023,3,8), "pending",'The Hazel Hide'),
                        Booking(3, 3, 3, 3, datetime.date(2023,3,11), datetime.date(2023,3,15), "pending", 'Entire Contemporary Barn'),
                        Booking(4, 4, 2, 4, datetime.date(2023,3,21), datetime.date(2023,3,27), "confirmed", 'Coloc All Included Febvotte-Marat'),
                        Booking(5, 5, 1, 5, datetime.date(2023,3,1), datetime.date(2023,3,3), "confirmed", '2RJ2- Hyper center.')]
    
def test_find(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    booking = repo.find(1)
    assert booking == Booking(1, 1, 5, 1, datetime.date(2023,3,1), datetime.date(2023,3,5), "pending", 'Chestnut Eco Lodge Woodland Escape')

def test_create(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    new_booking = repo.create(Booking(None, 1, 2, 1, datetime.date(2023,4,1), datetime.date(2023,4,5), None, "greenhouse"))
    result = repo.find(new_booking.id)
    assert result == Booking(6, 1, 2, 1, datetime.date(2023,4,1), datetime.date(2023,4,5), "pending", "greenhouse")

def test_delete(db_connection): 
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    booking_to_delete = Booking(None, 1, 2, 1, datetime.date(2023,4,1), datetime.date(2023,4,5), "pending", "greenhouse")
    repo.create(booking_to_delete)
    repo.delete(booking_to_delete)
    assert repo.all() == [Booking(1, 1, 5, 1, datetime.date(2023, 3, 1), datetime.date(2023,3,5), "pending",'Chestnut Eco Lodge Woodland Escape' ),
                        Booking(2, 2, 4, 2, datetime.date(2023,3,5), datetime.date(2023,3,8), "pending", 'The Hazel Hide'),
                        Booking(3, 3, 3, 3, datetime.date(2023,3,11), datetime.date(2023,3,15), "pending", 'Entire Contemporary Barn'),
                        Booking(4, 4, 2, 4, datetime.date(2023,3,21), datetime.date(2023,3,27), "confirmed", 'Coloc All Included Febvotte-Marat'),
                        Booking(5, 5, 1, 5, datetime.date(2023,3,1), datetime.date(2023,3,3), "confirmed", '2RJ2- Hyper center.')]


