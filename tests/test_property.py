from lib.property import Property

'''
As a user, I want to have a property with all its details
'''

def test_initializer():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', False)
    assert property.id == 1
    assert property.name == 'Nice Cottage'
    assert property.description == 'Nice Cottage'
    assert property.price == 100
    assert property.user_id == 'George' #possibly user_id
    assert property.booked_status  == False
    
def test_equal():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', False)
    property2 = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', False)
    assert property == property2

def test_format_correctly():
    property = Property(1, 'Nice Cottage', 'Nice Cottage', 100, 'George', False)
    assert str(property) == "Nice Cottage\n Nice Cottage\n £100\n Owner: George"
    
    