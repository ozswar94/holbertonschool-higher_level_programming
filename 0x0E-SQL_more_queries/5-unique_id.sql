-- create table unique_id with id has by default 1 and uniq
CREATE TABLE IF NOT EXISTS unique_id (
	id INTEGER DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
