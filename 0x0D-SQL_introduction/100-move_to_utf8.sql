-- converts the database to UTF8
ALTER DATABASE 
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name 
TEXT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
