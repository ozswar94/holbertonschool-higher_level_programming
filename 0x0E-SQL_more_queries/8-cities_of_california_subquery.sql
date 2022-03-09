-- select between 2 tables
SELECT cities.id, cities.name FROM states, cities WHERE states.name='California' AND cities.state_id=states.id;
