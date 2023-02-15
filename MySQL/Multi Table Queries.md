# KDT 2기 2월 15일 학습 내용

테이블을 분리하는 이유? 관리하기 편하도록
=> 테이블을 분리하면 관리는 용이해질 수 있으나 출력 할 때는 테이블 한 개만을 출력할 수 없어서 다른 테이블과 연결지어 출력해야한다.
=> JOIN 사용

# JOIN
둘 이상의 테이블에서 데이터를 검색하는 방법

## JOIN의 종류
- INNER JOIN
- OUTER JOIN
    - LEFT JOIN
    - RIGHT JOIN
- CROSS JOIN

## INNER JOIN
- 교집합
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

```SQL
SELECT select_list
FROM main_table
INNER JOIN sub_table
    ON main_table.fk = sub_table.pk;
```
- FROM에는 메인 테이블 지정
- INNER JOIN에는 메인 테이블과 조인할 테이블 지정
- ON에는 조인 조건을 작성
    - main_table과 sub_table의 PK값이 서로 같은 것끼리 묶음

```sql
SELECT title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```
SELECT 키워드에 id를 추가하면 에러가 난다.
=> 왜? articles과 users 테이블 모두 id를 필드로 가지고 있기 때문에 컴퓨터 입장에서 누구의 id인지 헷갈리는 것. `테이블.field`로 지정해준다.

에러 ❌
```sql
SELECT id,title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```
정상 작⭕
```sql
SELECT articles.id,title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```
## LEFT JOIN
-왼쪽 테이블 일단 모두 출력 + 교집합까지 출력
- [OUTER]는 선택 사항을 의미
- 왼쪽 테이블에서 교집합과 매치되는 레코드가 없으면 NULL로 채워진다.
```SQL
SELECT select_list
FROM left_table
LEFT [OUTER] JOIN right_table
    ON left_table.fk = right_table.pk;
```
```SQL
SELECT *
FROM articles
LEFT JOIN users
 ON articles.userId = users.id;
 ```
