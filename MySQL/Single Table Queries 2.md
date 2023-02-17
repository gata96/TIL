# KDT 2기 2월 13일 학습 내용

## 3. Filtering data
데이터를 필터링하여 중복 제거, 조건 설정 등 SQL Query를 제어하기

### Filtering data 관련 Keywords
- Clause
    - DISTINCT
    - WHERE
    - LIMIT

- Operator
    - BETWEEN
    - IN
    - LIKE
    - Comparison
    - Logical


✅ DISTINCT : 중복 제거
- SELECT 키워드 바로 뒤에 작성
- SELECT DISTINCT 키워드 다음에 유일했으면 좋겠는 하나 이상의 필드를 선택

```SQL
SELECT DISTINCT
    field
FROM
    table_name
ORDER BY
    field;
```

✅ WHERE : PYTHON의 IF와 같은 역할. 조건문
- FROM 키워드 뒤에 위치
```SQL
SELECT DISTINCT
    field
FROM
    table_name
WHERE
    조건;
```
조건 예시
```SQL
WHERE
    jobtitle != 'Sales Rep'
```
```SQL
WHERE
    jobtitle >= 3 AND coffee = 'Sales Rep'
```
```SQL
WHERE
    jobtitle >= 3 OR coffee = 'Sales Rep'
```
✅ BETWEEN A AND B
- A 이상 B 이하
- WHERE 절 다음에 ORDER BY를 쓴다.

```SQL
WHERE
    office BETWEEN 1 AND 4
ORDER BY office;
-- 'office 값이 1이상 4이하인 값'
```
✅ IN
- 1 또는 3 또는 4
```SQL
WHERE
    office IN (1,3,4)
```
✅ NOT IN
- 1과 3과 4가 아닌 데이터
```SQL
WHERE
    office NOT IN (1,3,4)
```
<BR>

✅ LIKE : 같이 특정 패턴에 일치하는지 확인
- 예시1 '테이블 employees에서 lastName 필드 값이 son으로 끝나는 데이터의 lastName, firstName을 조회'
```SQL
SELECT 
    lastName, firstName
FROM 
    employees
WHERE 
    lastName LIKE '%son';
```

- 예시2 '테이블 employees에서 lastName 필드 값이 4자리면서 y로 끝나는 데이터의 lastName, firstName을 조회'

```SQL
SELECT 
    lastName, firstName
FROM 
    employees
WHERE
    firstName LIKE '___y';
```
```SQL
WHERE YEAR(joined) = '2021' 
    
WHERE JOINED LIKE '2021%'
--이 둘은 같은 결과를 출력한다.
```

<BR>

✅ Wildcard Characters

'%' : 0개 이상의 문자열과 일치하는지 확인

'_' : 단일 문자와 일치하는지 확인

✅ Comparison Operators

=, >=, <=, IS, LIKE, IN, BETWEEN, AND

✅ Logical Operators

AND(&&), OR(||), NOT(!)

✅ LIMIT : 데이터 구간을 잘라서 출력하기

예시 1
```SQL
SELECT
    ..
FROM
    ..
LIMIT 3,5;
```
=> 4번째 데이터 부터 총 5개의 데이터를 출력
출력: 4,5,6,7,8

예시 2
테이블 customers에서 contactFirstName, creditLimit 필드 데이터를 creatLimit 기준 내림차순으로 7개만 조회
```sql
SELECT contactFirstName, creditLimit
FROM customers
ORDER BY creatLimit DESC
LIMIT 7;
```
=> ORDER BY 한 다음에 LIMIT

예시 3

4번째부터 7번째까지 데이터 조회
```sql
SELECT contactFirstName, creditLimit
FROM customers
ORDER BY creatLimit DESC
LIMIT 3,4;
```
```SQL
LIMIT 3,4
LIMIT 4 OFFSET 3;
-- 이 둘은 서로 동일한 코드
```
<BR>

## 4. Grouping data
GROUP BY
- 레코드를 그룹화하여 요약본 생성 
- SUM, AVG, MAX, MIN, COUNT와 함께 쓰인다.
- 중복을 제거한다.

```sql
-- jobTitle 필드를 그룹화
SELECT jobTitle
FROM employees
GROUP BY jobTitle;
```
```sql
--count 함수는 해당 필드가 몇번 나오는지 카운트해준다.
SELECT jobTitle, COUNT(*)
FROM employees
GROUP BY jobTitle;
```
```sql
-- country필드를 그룹화하여 각 그룹에 대한 creditLimit 평균 값을 내림차순 조회
SELECT country, AVG(creditLimit) AS average
FROM customers
GROUP BY country
ORDER BY average DESC;
```
```sql
SELECT country,  AVG(creditLimit)
FROM customers
GROUP BY country
HAVING AVG(creditLimit) > 80000;
```
## 5. NULL 정렬
데이터에 NULL이 존재할 경우, 오름차순 정렬시 결과에 NULL이 먼저 온다.



