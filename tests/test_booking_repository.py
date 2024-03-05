from lib.booking_repository import BookingRepository
from lib.booking import Booking
import datetime

def test_all(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    bookings = repo.all()
    assert bookings == [Booking(1, 1, 5, 1, datetime.date(2023, 3, 1), datetime.date(2023,3,5)),
                        Booking(2, 2, 4, 2, datetime.date(2023,3,5), datetime.date(2023,3,8)),
                        Booking(3, 3, 3, 3, datetime.date(2023,3,11), datetime.date(2023,3,15)),
                        Booking(4, 4, 2, 4, datetime.date(2023,3,21), datetime.date(2023,3,27)),
                        Booking(5, 5, 1, 5, datetime.date(2023,3,1), datetime.date(2023,3,3))]
    
def test_find(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    booking = repo.find(1)
    assert booking == Booking(1, 1, 5, 1, datetime.date(2023,3,1), datetime.date(2023,3,5))

def test_create(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    db_connection.seed('seeds/bookingtable.sql')
    repo = BookingRepository(db_connection)
    new_booking = repo.create(Booking(None, 1, 2, 1, datetime.date(2023,4,1), datetime.date(2023,4,5)))
    result = repo.find(new_booking.id)
    assert result == new_booking

