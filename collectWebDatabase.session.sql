-- delete from collectweb_user;
-- delete from collectweb_admin;
-- delete from collectweb_picTest;
-- delete from collectWeb_questionTest;

SELECT * FROM collectWeb_picTest;
SELECT * FROM collectWeb_questionTest;
SELECT * FROM collectweb_user;
-- SELECT * FROM collectweb_admin;

-- UPDATE collectweb_admin
-- SET password = '12345'
-- WHERE id = '12345';


-- INSERT INTO collectweb_admin (id, password)
-- VALUES ('12345','12345');
SELECT * FROM collectweb_admin;


-- ALTER TABLE collectWeb_questionTest ADD COLUMN record_id INT AUTO_INCREMENT PRIMARY KEY;

-- DESCRIBE collectWeb_questionTest;


-- SHOW TABLES;  -- MySQL


-- CREATE TABLE collectweb_admin (
--     id VARCHAR(25) PRIMARY KEY,
--     password VARCHAR(25)
-- );



-- MySQL
-- CREATE TABLE collectWeb_picTest (
--     id VARCHAR(55) PRIMARY KEY,
--     testDate VARCHAR(20) NOT NULL DEFAULT '0000-00-00',
--     audio BLOB
-- );

-- CREATE TABLE collectWeb_questionTest (
--     id VARCHAR(55) PRIMARY KEY,
--     testDate VARCHAR(20) NOT NULL DEFAULT '0000-00-00',
--     todayDate INT NULL,
--     position INT NULL,
--     remember INT NULL,
--     calculate INT NULL,
--     memorize INT NULL,
--     named INT NULL,
--     repeating INT NULL,
--     commandOperate INT NULL,
--     wordOperate INT NULL,
--     writing INT NULL,
--     draw INT NULL,
--     notes VARCHAR(800) NULL,
--     audio BLOB
-- );

