# KDT 2기 2월 14일 학습 내용
DDL : Data Definition Language

목차
1. Create a table 
2. Delete a table  
3. Modifying table fields

# CREATE TABLE
```SQL
CREATE TABLE table_name(
    column1 data_type,
    column2 data_type,
    테이블 및 필드에 대한 제약 조건
);
```
```sql
CREATE TABLE examples(
    examID INT AUTO_INCREMENT,
    -- 필드와 데이터 타입을 공백 기준으로 설정
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL
    -- NULL값(빈 값)을 허용하지 않겠다.
    PRIMARY KEY (examID)
    -- 식별자 선언
);
SHOW COLUMNS FROM examples;
-- 데이터 테이블을 직관적으로 보여줌으로써 잘 생성됐는지 확인 할 수 있다.
```
테이블 업데이트는 자동으로 되지 않기 때문에 파일 트리에 별도의 버튼을 수동으로 눌러 새로 고침 해야한다. 

## 데이터 타입
|데이터 타입|예시|
|-|-|
|숫자형|INT, FLOAT|
|문자형|VARCHAR, TEXT|
|날짜형|DATE, DATETIME|

CHAR(50)과 VARCHAR(50)의 차이
CHAR(50) : 만약 입력되는 문자의 길이가 3이면 나머지 47칸을 전부 공백으로 50까지 채움
VARCHAR(50) : 만약 입력되는 문자의 길이가 3이면 3만큼만 자리를 채운다. (가변길이)
길이를 따로 정해주기 싫으면 'TEXT'를 쓰면 된다.

## 제약 조건
NOT NULL
- 해당 필드에 NULL 값을 허용하지 않겠다.
PRIMARY KEY
- 해당 필드를 기본키로 지정한다.
- 보통은 식별자를 SQL문 최하단에 작성한다.

## 속성
AUTO_INCREMENT
- 테이블의 기본 키 필드에 고유한 숫자를 부여
- 시작 값은 1이며 입력시 값을 생략하면 자동으로 1씩 증가
- 이미 사용한 값을 재사용하지 않음
- 기본적으로 NOT NULL 제약 조건을 포함

# DROP TABLE 
- 테이블을 삭제
```SQL
DROP TABLE table_name
```

# Modifying table fields
ALTER TABLE : 테이블 필드를 조작(생성, 수정, 삭제)
|ALTER TABLE|설명|
|-|-|
|ALTER TABLE ADD|필드 추가|
|ALTER TABLE MODIFY|필드 속성 변경|
|ALTER TABLE CHANGE COLUMN|필드 이름 변경|
|ALTER TABLE DROP COLUMN|필드 삭제|

