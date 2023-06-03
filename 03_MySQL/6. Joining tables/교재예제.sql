CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userID INT NOT NULL,
    PRIMARY KEY(id)
);

SELECT * FROM users;
SELECT * FROM articles;

INSERT INTO users(name)
VALUES ('SQL'), ('오은정'),('루카스');

INSERT INTO articles(title, content, userID)
VALUES 
	('제목1','내용1',1),
    ('제목2','내용2',2),
    ('제목3','내용3',4);