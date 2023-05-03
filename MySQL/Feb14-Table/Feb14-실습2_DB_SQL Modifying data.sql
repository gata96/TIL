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
	('Beemo','Jeong','1000-01-01',NULL,NULL,'beemo@hphk.kr'),
    ('Jieun','Lee','1993-05-16','Seoul','Korea',NULL	),
    ('Dami','Kim','1995-04-09','Seoul','Korea',NULL),
    ('Kwangsoo','Lee','1985-07-14','Seoul','Korea',NULL);
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
-- 문제 5 
-- 테이블 users 에서 country 필드가 NULL 인 모드 레코드의 country 필드 값을 Korea 로 변경하시오.
UPDATE users
SET country = 'Korea'
WHERE country IS NULL;
SELECT * FROM users;

-- 문제6
-- 테이블 users 에서 first_name 필드가 Beemo 인 레코드를 삭제하시오.
DELETE FROM
	users
WHERE
	first_name = 'Beemo';
    
SELECT * FROM users;

-- 문제7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo' and
    last_name = 'Lee';

-- 문제 8
DELETE FROM
	users
ORDER BY
	TIME(created_at) DESC
LIMIT 1;
