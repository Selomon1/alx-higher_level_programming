-- Script that creates the table unique_id
-- not fail if exists
CREATE table IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
