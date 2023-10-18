-- Script that creates the MySQL server user user_0d_1
-- the user exists, the script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED by 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@localhost;
FLUSH PRIVILEGES;
