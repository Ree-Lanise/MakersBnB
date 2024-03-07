DROP TABLE IF EXISTS bookings cascade;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INTEGER, 
    owner_id INTEGER, 
    guest_id INTEGER,
    starting_date DATE, 
    end_date DATE,
    status TEXT,
    name TEXT,
    FOREIGN KEY (property_id) REFERENCES properties(id) on delete cascade,
    FOREIGN KEY(owner_id) REFERENCES users(id) on delete cascade,
    FOREIGN KEY(guest_id) REFERENCES users(id) on delete cascade );

-- finally, we add any records that are needed for the tests to run
INSERT INTO bookings (property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES ( 
    1, 5, 1, '2023-03-01', '2023-03-05', 'pending', 'Chestnut Eco Lodge Woodland Escape'); 
INSERT INTO bookings (property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES ( 
    2, 4, 2, '2023-03-05', '2023-03-08', 'pending', 'The Hazel Hide'); 
INSERT INTO bookings (property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES ( 
    3, 3, 3, '2023-03-11', '2023-03-15', 'pending', 'Entire Contemporary Barn'); 
INSERT INTO bookings (property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES ( 
    4, 2, 4, '2023-03-21', '2023-03-27', 'confirmed', 'Coloc All Included Febvotte-Marat'); 
INSERT INTO bookings (property_id, owner_id, guest_id, starting_date, end_date, status, name) VALUES ( 
    5, 1, 5, '2023-03-01', '2023-03-03', 'confirmed', '2RJ2- Hyper center.'); 