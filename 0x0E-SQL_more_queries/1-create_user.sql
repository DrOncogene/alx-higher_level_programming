-- creates a new user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
 IDENTIFIED BY 'user_0d_1_pwd';
-- grants all permissions to all databases
GRANT ALL
   ON *.*
   TO 'user_0d_1'@'localhost';
