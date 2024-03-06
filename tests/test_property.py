from lib.property import Property
import datetime

'''
As a user, I want to have a property with all its details
'''

def test_initializer():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', datetime.date(2023,1,1),datetime.date(2023,12,31))
    assert property.id == 1
    assert property.name == 'Nice Cottage'
    assert property.description == 'Nice Cottage'
    assert property.price == 100
    assert property.user_id == 'George' #possibly user_id
    assert property.aval_start  == datetime.date(2023,1,1)
    assert property.aval_end  == datetime.date(2023,12,31)

def test_equal():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', datetime.date(2023,1,1),datetime.date(2023,12,31))
    property2 = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', datetime.date(2023,1,1),datetime.date(2023,12,31))
    assert property == property2

def test_format_correctly():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', datetime.date(2023,1,1),datetime.date(2023,12,31))
    assert str(property) == "Nice Cottage\n Nice Cottage\n £100\n Owner: George\n Available start date: 2023-01-01\n Available end date: 2023-12-31"
    
    