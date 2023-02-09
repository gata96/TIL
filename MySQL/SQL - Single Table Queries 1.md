# SQL Basics
학습목표
- 데이터베이스에서 SQL의 역할을 정의할 수 있다.
- SQL 명령의 종류를 동작에 따라 3가지 이상 열거할 수 있다.
- 표준 SQL 문법을 식별할 수 있다.

### Query
- 뜻: 질의, 질문
- '데이터 베이스에게 정보를 요청'하는 것
- SQL로 작성한 코드를 쿼리문(SQL문)이라고 한다.

## SQL (Structure Query Language)
- 구조적인 요청을 하는 언어? 즉, 테이블의 형태로 구조화된 관계형 데이터베이스에게 정보를 요청
- 컴퓨터와의 대화 -> 프로그래밍 언어 / 관계형 데이터 베이스와의 대화 -> SQL
- SQL은 데이터 베이스에 정보를 저장하고 처리하기(CRUD) 위한 데이터 베이스 전용 프로그래밍 언어이다. 

## SQL 표준
- 대부분 모든 RDBMS에서 SQL표준을 지원하나, RDBMS 별로 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의하자. 예를 들어, 오라클, MySQL 등 각 RDBMS 회사들은 서로 경쟁해야하므로 각자의 독자적인 기능이 존재할 수 있음

# SQL - Single Table Queries 1
## 학습목표
- 단일 테이블 내에서 SELECT문을 사용해서 테이블의 특정 결과를 반환할 수 있다. (SELECT FROM)
- SELECT문과 함께 쿼리 결과를 정렬 및 필터링 할 수 있다. (ORDER BY DESC|ASC)
- GROUP BY와 Aggregation Function을 사용해 각 데이터 값에 대한 계산된 단일 값을 그룹화하여 반환 할 수 있다.

## SQL Syntax
- SQL은 대소문자 구분하지 않는다.
    - 하지만, 대문자로 쓰는 것을 권장한다.
- 각 SQL 문장 끝에는 세미콜론(;)이 필요하다.
    - 세미콜론은 각 SQL 문장을 구분하기 때문


## 핵심
- 우리가 원하는 데이터를 얻기(반환하기) 위해서 SQL을 통해 데이터 베이스와 Talk해야함
- 단순히 SQL 문법을 암기하고 상황에 따라 실행만 하는 것이 아니라, SQL을 통해 관계형 데이터 베이스를 잘 이해하고 다루는 방법을 학습한다.


## SQL - Single Table Queries
1) Querying data
2) Sorting data
3) Filtering data
4) Grouping data


## SQL Statements
- SQL언어를 구성하는 가장 기본적인 코드 블록 
- 이 Statements는 SELECT, FROM 2개의 keyword로 구성됨

### 예시
```sql
SELECT column_name FROM table_name;
```

## SQL Statements 유형
- 데이터 베이스에서 수행 목적에 따라 대체로 4가지 범주로 나뉜다.

|유형|정의|역할|SQL 키워드|
|-|-|-|-|
|DDL (Data Definition Language)|데이터 정의|데이터 구조 및 형식를 정의|CREATE<br>DROP <br>ALTER|
|DQL (Data Query Language)|데이터 검색|읽기|SELECT|
|DML (Data Manipulation Language)|데이터 조작|CUD|INSERT<br>UPDATE<br>DELETE|
|DCL (Data Control Language)|데이터 제어|사용자의 권한이나 계정을 컨트롤|COMMIT<br> ROLLBACK <br>GRANT <br>REVOKE|



⭐ DQL에서 SELECT는 원본 테이블의 데이터를 조작하지 않고, 오로지 `조회`만 한다는 것을 기억해야한다.

## 1. Querying data
SELECT statement (데이터를 조회하고 읽을 수 있음, CRUD에서 R 역할)

- SELECT 키워드 다음에는 field를 선택
- FROM 키워드 다음에는 Table을 지정
- 들여쓰기 상관 1도 없고, 어디서 문장이 끝나는지가 중요하다. 하지만 들여쓰기 해주면 가독성이 높아진다.

✔️example 1

✅ 모두 가능 
```sql
SELECT
    field
FROM
    table_name;
```
```sql
SELECT field FROM table_name;
```
```sql
SELECT
field
FROM
table_name;
```
✔️example 2 -- table내의 field 2개 출력
```sql
SELECT
    field1, field2
FROM
    table_name;
```

✔️example 3 -- table내의 모든 필드 출력
```sql
SELECT * FROM table_name;
```
✔️example 4 -- AS 키워드를 사용해서 field명에 바꿔서 출력할 수 있다. 원본 데이터의 해당 field명은 변함이 없다.
```sql
SELECT
    field AS 바꾸고자하는 이름
FROM
    table_name;
```

⭐ AS로 field명을 바꿔서 출력할 때, SELECT문으로 데이터를 조회하는 것이지 조작하는 것이 아니다. 그러므로 원본 table의 수정이나 조작이 없다.

⭐ 현재 우리는 오로지 DQL만 보고 있다. 이 말은 즉슨, 데이터를 조작하는 것이 아닌 원본 데이터는 건들지 않고, 출력창에 보이는 것. 즉, `조회`만 보고 있기 때문에 AS를 사용해서 field의 이름을 바꾼다고 해도 출력창에만 그렇게 보이는 것일 뿐, 원본 데이터는 전혀 변함이 없다는 것을 기억하자.

✔️example 5 -- field끼리 연산 가능. 프로그래밍이 되기위한 조건 첫번째가 연산이 가능해야한 것이기 때문에 SQL에서도 연산이 가능하다.
```sql
SELECT
    field1 * field2 AS 주문 총액
FROM
    table_name;
```
⭐ 주문총액과 같이 AS를 사용해서 별명을 붙힐 때, '주문총액' 처럼 따옴표를 붙히지 않는 것이 특징이다. 따옴표를 붙히면 문자 자체로 인식하기 때문에 주의 필요.

❗NULL : database에서 data(값)이 없음을 표현하는 값
    - 파이썬에서의 None(값)과 같은 기능

<br>

## 2. sorting data
- 조회 결과인 레코드를 정렬
- ORDER BY 절 : 조회 결과의 레코드를 정렬(오름차순, 내림차순)
- SELECT 부터 ORDER BY까지 ; 없이 쭉 쓰고 맨 마지막에만 ;쓴다.

```SQL
SELECT
    field
FROM
    table_name

ORDER BY
    field1 [ASC|DESC],
    field2 [ASC|DESC],
    ...;
```
❗[]의 경우 대괄호를 직접 쓰라는 게 아니라, 옵션이니 선택적으로 쓰라는 말이다.

ASC: 오름차순(기본 값) -> 생략 가능하다는 뜻
DESC: 내림차순

✔️example 1 -- employees 테이블에서 firstName 필드를 출력한 후, 오름차순으로 정렬
```SQL
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName;

```
✔️example 2 -- employees 테이블에서 firstName 필드를 출력한 후, 내름차순으로 정렬
```SQL
SELECT
    firstName
FROM
    employees
ORDER BY
    firstName DESC;

```
✔️example 3 -- employees 테이블에서 lastName 필드를 내림차순으로 정렬한 다음, 그것을 기준으로 firstName 필드를 오름차순으로 정렬
```SQL
SELECT
    lastName, firstName
FROM
    employees
ORDER BY
    lastName DESC,
    firstName;

```
✔️example 4 -- orderdetails 테이블에서 totalSales 필드를 기준으로 내림차순으로 정렬한 다음 productCode, totalSales 필드의 모든 데이터를 조회
(단, totalSales 필드는 quantityOrdered와 priceEach 필드를 곱한 결과값)
```SQL
SELECT
    productCode,
    quantityOrdered * priceEach AS totalSales
FROM
    orderdetails
ORDER BY
    totalSales DESC;
```


