# KDT 2기 2월 8일 학습 내용

# 데이터 베이스
## 데이터 베이스의 역할 : CRUD
- Create : 저장
- Read: 조회
- Update : 업데이트
- Delete : 삭제

<br>

# 관계형 데이터베이스 용어

1. Table (aka Relation)
- 데이터를 기록하는 곳
- 간혹 Relation이라고 하기도 한다.

<br>

2. [Field(aka Column, Attribute(속성))](./img/10.png)
- 열
- 각 필드에는 데이터의 값이 아닌 `데이터 타입`이 지정됨
- 관계형 데이터베이스에서는 Row와 Column이라는 용어를 잘 쓰지 않는다.
4개의 Field
id(정수), 이름,청구지,주소지(문자열)

<br>


3. [Record(aka Row, Tuple)](./img/11.png)
- 행
- 각 레코드에는 구체적인 `데이터 값`이 저장됨

<br>

4. [Database(aka Schema)](./img/12.png)
- 테이블의 집합(Set of tables)

<br>

5. [Primary Key(기본키)](./img/13.png)
- 각 레코드의 고유한 값
- 관계형 데이터베이스에서 각각의 레코드를 구분할 수 있는 식별자
- 식별자이기에, 중복이 있으면 안되고 유일해야 한다.

<br>

6. [Foreign Key(외래키)✨](./img/14.png)
- 테이블들의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 각 레코드에서 서로 다른 테이블 간의 `관계를 만드는 데 ` 사용
- 관계형 데이터 베이스에서의 핵심

<br>

Data를 잘 다루기 위해서는 Table을 잘 다뤄야하고, Table을 다루기 위해서는 Database를 다뤄야하는데 Database 자체를 다루는 건 쉽지않아서, Database를 관리할 수 있도록 도와주는 Tool이 존재한다.

<br>
<br>

# RDBMS (Relational Database Management System)
- 관계형 데이터베이스를 관리하는 소프트웨어 프로그램

<br>

## DBMS (Database Management System)
- 데이터의 저장 및 관리를 용이하게 해주는 시스템
- 데이터 베이스와 사용자 간의 인터페이스 역할
    - 사용자가 직접 DB에 접근하는 것이 어려우니, 중간 다리인 RDBMS를 통해 DB에 접근한다.
    - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있게 해준다.

<br>

## 대표적인 RDMBS 
(목적: 관계형 데이터 베이스를 잘 관리할 수 있도록 도와주는 것)
- `MYSQL`
- PostgreSQL
- Oracle Database
- MS SQL Server

<br>

## MYSQL
- 가장 널리 사용되는 오픈 소스 RDBMS
- 특징
    - 다양한 운영체제(Window, Mac, Linux..)
    - 여러 프로그래밍 언어를 위한 다양한 API 제공
        - DB를 관리하기 위한 언어가 따로 존재하지만, 사용자의 편의를 위해 파이썬, 자바 등과 같은 여러 프로그래밍 언어로도 관리할 수 해주는 것이 MYSQL의 역할이다.
    - MySQL Workbench Tool을 통해 그래픽 인터페이스를 제공(GUI)
        - 그게 안되면 cmd 창에서 눈 껌뻑이며 타이핑 해야한다. 너무 불-편

### [MYSQL 구조](./img/15.png)
- Table < Database < Database Server(MySQL)
- Table을 조작하고 Table의 집합인 Database를 잘 관리, 백업, GUI 툴을 제공하는 시스템들(RDBMS) 중 MySQL을 택할 것이다.
- 참고. Database Server와 RDBMS는 약간 다른 개념인데, Server라는 이름이 붙은 이유는 on/off 기능 때문이다. MySQL은 on을 해야 사용할 수 있고, 사용하지 않을 때 off할 수 있다. 반면, server형태가 아닌 파일 형태 처럼 on/off 기능이 없는 것도 있다.
