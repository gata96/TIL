# KDT 2기 2월 15일 학습 내용

테이블을 분리하는 이유? 관리하기 편하도록
=> 테이블을 분리하면 관리는 용이해질 수 있으나 출력 할 때는 테이블 한 개만은 출력할 수 없어서 다른 테이블과 연결지어 출력해야한다.

✅ JOIN 사용

# JOIN
둘 이상의 테이블에서 데이터를 검색하는 방법

## JOIN의 종류
- INNER JOIN
- OUTER JOIN
    - LEFT JOIN
    - RIGHT JOIN
- CROSS JOIN
    - 합집합 UNION
    - 교집합 없이 LEFT만
    - 교집합 없이 RIGHT만
    

## INNER JOIN
- 교집합
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

```SQL
SELECT select_list
FROM main_table
INNER JOIN sub_table
    ON main_table.fk = sub_table.pk;
```
- FROM 뒤에 메인 테이블
- INNER JOIN 뒤에 메인 테이블과 조인할 서브 테이블
- ON 뒤에는 main_table과 sub_table의 FK,PK(공통키)값을 적어준다.

```sql
SELECT title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```

에러 ❌
```sql
SELECT id,title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
-- SELECT 키워드에 id를 추가하면 에러가 난다.
=> 왜? articles과 users 테이블 모두 id를 필드로 가지고 있기 때문에 컴퓨터 입장에서 누구의 id인지 헷갈리는 것. `테이블.field`로 지정해준다.
```
정상 작동⭕
```sql
SELECT articles.id,title, content, name
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```
## LEFT JOIN
- 왼쪽 테이블 전부 + 교집합
- [OUTER]는 선택 사항
- 왼쪽 테이블에서 교집합과 매치되는 레코드가 없으면 NULL로 채워진다.
```SQL
SELECT select_list
FROM left_table
LEFT [OUTER] JOIN right_table
    ON left_table.공통키 = right_table.공통키;
```
```SQL
SELECT *
FROM articles
LEFT JOIN users
 ON articles.userId = users.id;
 ```
 ## RIGHT JOIN
- 오른쪽 테이블 전부 + 교집합
- 매치되는 코드가 없으면 NULL 표시

```SQL
SELECT *
FROM right_table
LEFT JOIN left_table
    ON right_table.공통키 = left_table.공통키;
```
## 합집합 UNION
```SQL
SELECT * FROM left_table
LEFT JOIN right_table ON left_table.공통키 = right_table.공통키

UNION

RIGHT JOIN right_table ON left_table.공통키 = right_table.공통키;
```

## 교집합 빼고 LEFT만
```sql
SELECT * FROM left_table
LEFT JOIN right_table
    ON left_table.공통키 = right_table.공통키
WHERE right_table.공통키 IS NULL;
```

## 교집합 빼고 RIGHT만
```sql
SELECT * FROM right_table
RIGHT JOIN left_table
    ON left_table.공통키 = right_table.공통키
WHERE left_table.공통키 IS NULL;

