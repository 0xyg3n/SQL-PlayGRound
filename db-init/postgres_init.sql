CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, username TEXT, password TEXT);
INSERT INTO users(username,password) VALUES('admin','password');
