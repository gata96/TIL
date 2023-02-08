# Workbench 활용 가이드
## Workbench 활용 MYSQL 접속 방법

1. 실습용 데이터 베이스 파일(sample_db.sql) 다운로드


<br>

2. Workbench에서 실습용 데이터 베이스 추가
- [MYSQL 접속](./Image/1.png)
- [Administration -> Data Import/Restore](./Image/2.png)
- [해당 데이터 베이스 import하기 ](./Image/3.png)
Import from Self-Contained File -> ''' -> Start Import
- [Import 성공화면 확인](./Image/4.png)

<br>

3. [실습용 데이터 베이스 확인](./Image/5.png)
- Schemas 클릭
-> 새로고침 버튼 클릭
-> 데이터 베이스 classicmodels 확인

<br>

4. [쿼리(Query) 실행 테스트](./Image/6.png)
- classicmodels 데이터 베이스 선택(더블 선택)
- Query 에디터 클릭
- 쿼리문 입력
```sql
SELECT * FROM customers;
```
- [쿼리 실행](./Image/7.png)
- 출력 확인

<br>

5. 한글 입력 설정
❗MySQL은 기본적으로 한글 데이터 입력이 되지 않기 때문에 추가 설정 필요
- [데이터 베이스 옆 도구 모양 클릭](./Image/8.png)
- [utf8과 utf8_bin 으로 변경 - Apply 클릭](./Image/9.png)


