# KDT 2기 12월 27일 학습 내용

## 윈도우

1. 바탕화면에 `TIL` 폴더를 만든다.
2. 우클릭으로 code로 열기를 누른다.
    - 혹시나, 윈도우 11이라면 더 많은 옵션 표시를 확인한다.
3. 우클릭해서 NEW file, 확장자는 .md, 파일명은 자유롭게

<br>

# 마크다운 기반의 문서 작성법

<br>

# 마크다운(Markdown)이란?

1. 웹상에서 글을 쓰기 위해 도와주는 **글쓰기 도구(서식,포맷,양식)**
2. HTML를 몰라도 HTML형식(마크업 언어)로 바꿔줄 수 있다.
    - 마크업 언어(Markup language)의 예시인 HTML의 'ML'이 Markup language이다.
3. 간단한 문법으로 글을 쓰는 사람과 읽는 사람 모두 쉽도록 도와준다.
4. 확장자: 한글(hwp), 워드(docx), 마크다운(md)
5. READ.me로 이름을 설정하면 깃허브 포맷에 맞게 설정된다(실습해보기)
6. 정적사이트생성기 (Static site generator) 기반 블로그; 깃허브에서 기록을 남기고 블로그 형태로 변환 할 수 있다.
7. 주피터 (데이터분석,머신러닝ML/딥러닝DL) 분석 결과를 정리할 수 있는 tool과 노션도 마크다운 기반의 Software이다.

<br>
<br>

# Heading(#)
### 1. 문서의 제목이나 소제목
### 2. 단순히 글자 크기를 조절하기 위함이 아닌, 서론, 본론, 결론 등 문단을 나눌 때 쓴다. 
    # 서론  ## 개요
            ## 배경 ###국내
                    ###국외
            ## 목적

    # 본론(1,2,3)

    # 결론(강조, 결과)


# List: 목록
### 1. 하이픈(-) = 별표(*)
### 2. tab 하이픈 = tab 별표
    shift + tab 빠져나오기
### 3. 넘버링(1,2,3)
<br>

### 점심메뉴
* 김치 볶음밥
* 계란 후라이
- 햄버거
    - 치즈 2장 <!--tab-->
    * 패티  2장
    - 양상추
- 음료  <!--#shift + tab-->
    - 제로 펩시


<br>


# 코드블록(''' ''')
### 1. 키보드 물결 밑에 있는 아이콘 3개
### 2. 검정 배경 창 (주로 python 코드 칠 때 사용)
### 3. 글을 강조할 수 있다.
### ~~4. 들여쓰기(tab)해도 같은 기능을 가진다.~~


```python
print('hello')
#주석
```
```html
# html에서는 샵이 주석이 아니다
<!-- 주석 -->
```

```json
{
"안녕 나는 은정이야"
}
```

<br>

# 인라인 코드블록(' ') 
### 1. 물결 밑의 아이콘 1개
### 2. 강조용
<br>

> 마크다운은 `마크업 언어` 입니다. `print`는 파이썬에서 출력을 하는 함수입니다.

<br>

# Link :링크 주소
### [문자열](url)
<br>

​[구글](https://google.com)
<br>

​[네이버](https://naver.com)
>구글,네이버 홈페이지로 이동 할 수 있다.

<br>

# 새로운 파일, 폴더 생성

### [a 폴더](a/) ; a 폴더 생성
### [b 파일](b.md) ; b 파일생성
### [a 폴더 a.txt](a/a.txt) ; a 폴더에 a파일 생성

<br>

# 이미지
- 보노보노.png를 보여주는 문법
<br>
![보노보노](C:\Users\skswo\OneDrive\바탕 화면\TIL\image.jpg)
image.png
* 미켈레.png를 보여주는 문법
<br>
![](d/미켈레.jpg)
![1](d/미켈레.jpg)

>이미지 파일들이 Markdown과 같은 상의 폴더 안에 존재해서 한다. 경로 잘못 설정하면 사진이 깨진다.

> 대괄호 안의 숫자1은 생략할 수 있다.

<br>

# 인용, 정의 '>'
> 중요한 것은 꺾이지 않는 마음이다.

<br>

# 테이블

|식단|운동|
|----|----|
|샐러드|플랭크|
|귀리|실내사이클|

<br>

# 텍스트 강조

### 굵게(Bold): ** **
### 기울임(Italic): * * 또는 _ _

<br>

> 중요한 것은 **꺾이지 않는 마음** 입니다.

<br>

> *건강하게 먹고 운동하는 것* 이 최고의 다이어트 방법입니다.
> _건강하게 먹고 운동하는 것_
<br>

# 수평선
--- `대쉬`

*** `별표`

___ `언더대쉬`

<br>

# 취소선
문자 양쪽으로 ~~ 붙이기.
> ~~이 메세지는 삭제 되었습니다.~~

<br>

# 마크다운 추가자료

- GitHub Flavored Markdwon
- Mastering Markdown
- Markdown Guide

<br>

## 💡 하루일지
처음으로 스스로 완주해본 코딩 과제였는데 뿌듯했다. 속도가 조금 느린 것 같긴 한데, 그래도 잘 이해하고 과제도 잘 마무리 한것 같아서 기분이 좋다. 중요한 것은 오늘 배운 것을 추후에 잊어버리지 않도록 하기 위해 매일 매일 복습하는 것이 중요할 것 같다. 또한, 기록의 힘을 믿기 때문에 꾸준히 발자취를 남겨서 성장해가는 모습을 보고 싶다. 내일 github 수업이 있다고 하셨는데, github에 꾸준히 기록할 수 있도록 **how to use** 를 얼른 배워야할 것 같다.
두번째 과제를 아직 못해서 그냥 잘까도 생각했는데, 이대로 자면, 복습도 완전히 못하고 과제도 못한게 되어서 내일이 되면 새로운 내용이 많이 나오기 때문에 더 벅차질 것 같아서 피곤하지만 끝까지 하려고 노력했다. **오늘 공부한 건 오늘 끝내기!! ** 뿌듯쓰!!




