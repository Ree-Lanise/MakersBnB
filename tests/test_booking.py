from lib.booking import Booking

def test_initializer():
    booking = Booking(1, 1, 5, 1, '2023-03-01', '2023-03-05')
    assert booking.id == 1
    assert booking.property_id == 1
    assert booking.owner_id == 5
    assert booking.guest_id == 1
    assert booking.starting_date == '2023-03-01'
    assert booking.end_date == '2023-03-05'

def test_equality():
    booking1 = Booking(1, 1, 5, 1, '2023-03-01', '2023-03-05')
    booking2 = Booking(1, 1, 5, 1, '2023-03-01', '2023-03-05')
    assert booking1 == booking2

def test_formatting():
    booking = Booking(1, 1, 5, 1, '2023-03-01', '2023-03-05')
    assert str(booking) == "Booking(1, 1, 5, 1, 2023-03-01, 2023-03-05)"