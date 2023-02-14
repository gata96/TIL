SHOW COLUMNS FROM posts;
-- 문제1
CREATE TABLE posts(
    postID INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postID)
);
-- 문제2
ALTER TABLE posts
ADD writer VARCHAR(100) DEFAULT 'Anonymous',
ADD created_at DATETIME DEFAULT CURRENT_TIMESTAMP;

-- 문제3
ALTER TABLE posts
MODIFY content text NULL;

-- 문제4
ALTER TABLE posts
DROP COLUMN writer;

-- 문제5
DROP TABLE posts;

-- 문제6
CREATE TABLE posts(
    postID INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (postID)
);

-- 문제7
DROP TABLE posts;