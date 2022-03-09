-- create table id_not_null with id has by default 1
CREATE TABLE IF NOT EXISTS id_not_null (
	id INTEGER DEFAULT 1,
	name VARCHAR(256)
);
