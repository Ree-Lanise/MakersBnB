DROP TABLE IF EXISTS properties cascade;
DROP SEQUENCE IF EXISTS properties_id_seq;

CREATE SEQUENCE IF NOT EXISTS properties_id_seq;
CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT, 
    price INTEGER, 
    user_id INTEGER,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    available_start DATE,
    available_end DATE);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES ( 
    'Chestnut Eco Lodge Woodland Escape', 'House with garden', 101, 1, '2023-01-01', '2024-01-01'); 
INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES ( 
    'The Hazel Hide', 'Luxury Eco A-Frame Cabin', 240, 3, '2023-01-01', '2024-01-01'); 
INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES ( 
    'Entire Contemporary Barn', 'Barn in Essex', 550, 5, '2023-01-01', '2024-01-01'); 
INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES ( 
    'Coloc All Included Febvotte-Marat', 'Room in Tours', 463, 1, '2023-01-01', '2024-01-01'); 
INSERT INTO properties (name, description, price, user_id, available_start, available_end) VALUES ( 
    '2RJ2- Hyper center.', 'Entire rental unit in Tours', 472, 4, '2023-01-01', '2024-01-01'); 