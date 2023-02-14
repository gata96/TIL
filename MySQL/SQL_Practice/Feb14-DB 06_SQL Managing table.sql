-- 문제1
CREATE TABLE users(
	userID INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (userID)
);
SHOW COLUMNS FROM users;
DROP TABLE users;
-- 문제2
INSERT INTO 
	users (first_name,last_name,birthday,city,country,email)
VALUES
	('Beemo','Jeong','1000-01-01','','','beemo@hphk.kr'),
    ('Jieun','Lee','1993-05-16','Seoul','Korea',''	),
    ('Dami','Kim','1995-04-09','Seoul','Korea',''),
    ('Kwangsoo','Lee','1985-07-14','Seoul','Korea','');
SELECT * FROM classicmodels.users;

-- 문제3

INSERT INTO 
	users (first_name,last_name,birthday,city,country,email)
VALUES
	('은미','김','1996-01-01','Lisbon','Portugal','');

-- 문제 4
UPDATE
	users
SET
	first_name = '은정',
    last_name = '오',
    birthday = '1996-11-11'
WHERE
	userID = 5;
-- 문제 5 😓
SET SQL_SAFE_UPDATES =0;
UPDATE
	users
SET
	country = REPLACE(country,'NULL', 'Korea');
	
SELECT * FROM classicmodels.users;

-- 문제6 😓
DELETE FROM
	users
WHERE
	userID = 1;
SELECT * FROM users;

-- 문제7
DELETE FROM
	users
WHERE
	userID = 4;

-- 문제 8
DELETE FROM
	users
ORDER BY
	TIME(created_at) DESC
LIMIT 1;
