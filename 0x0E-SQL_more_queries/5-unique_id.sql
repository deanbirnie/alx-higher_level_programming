-- Creates the table "unique_id" in db (passed as argument)
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256)
       );
