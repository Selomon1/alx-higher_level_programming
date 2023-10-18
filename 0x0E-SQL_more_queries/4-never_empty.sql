-- Script that creates the table id_not_null
-- not fail if exists
CREATE table IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
