USE sql_injection_lab;
IF OBJECT_ID('users','U') IS NULL BEGIN
  CREATE TABLE users(id INT IDENTITY PRIMARY KEY, username VARCHAR(50), password VARCHAR(50));
  INSERT INTO users(username,password) VALUES('admin','password');
END
