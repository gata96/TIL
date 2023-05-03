# KDT 2기 2023년 1월 9일 학습 내용

# Methods (메서드)

`학습 목표`
- 메서드와 함수의 차이점 알기
- 파이썬 주요 객체 타입의 메서드 비교 및 활용하기
- 메서드 별 필수 인자와 결과값 예측하기

| |함수|변경 가능|반복 가능|
|-|-|-|-|
|시퀀스|string|X|O|
||tuple|X|O|
||range|X|O|
||list|O|O|
|컬렉션|set|O|O|
||dictionary|O|O|

<br>

## String type(문자열)
|문법|설명|
|-|-|
|s.find(x)|x의 첫 번째 위치를 반환. 없으면 -1을 반환|
|s.index(x)|x의 첫 번째 위치를 반환. 없으면 오류|
|s.isalpha(x)|알파벳 여부|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|
|s.replace(old,new)|old 글자를 new글자로 바꿔줌|
|s.replace(old,new,count)|count 개수 만큼 바꿔줌|

<br>


### .find(x)
```python
'apple'.find('p')
# 1

'apple'.find('k')
# -1
```

### .index(x)
```python
'apple'.index('p')
# 1

'apple'.find('k')
# ValueError: substring not found
```

### .isalpha()

```python
'abc'.isalpha() # True
'Ab'.isupper() # False
'ab'.islower() # True
```

### .replace(old,new)

```python
'coone'.replace('o','a')  # caane
'woooowoo'.replace('o','!',2) # w!!oowoo
```
### .strip()
- strip: 양쪽 제거, lstrip: 왼쪽 제거, rstrip: 오른쪽 제거
- .strip('문자'): 해당 문자 제거


### .split() : `공백을 기준으로` 문자열을 -> 리스트로 바꾼다.

문자열.split()
문자열.split('구분자')
문자열.split('구분자',분할횟수)

```python
s = 'banana'
print(s.split()) # ['banana']

s = 'b a n a n a'
print(s.split()) # ['b', 'a', 'n', 'a', 'n', 'a']

s = 'tomato, peach'
print(s.split(',')) # ['tomato', ' peach']
print(s.split(sep = ',')) # ['tomato', ' peach'] # 출력 결과 같다.

s = 'a,b,c,d,e,f,g'
print(s.split(',',3)) # ['a', 'b', 'c', 'd,e,f,g']
```

### 구분자.join([문자열]) : 컨테이너 요소를 구분자로 합쳐 `문자열`로 반환

```python
print('!'.join(['3','5'])) # 3!5
```
<br>

# 리스트(List)
- 변경 가능 한 값의 나열된 자료형
- 순서있음. 서로 다른 타입의 요소를 가질 수 있음
- 변경 가능, 반복 가능
- 대괄호[]로 사용, 원소는 콤마로 구분

    [1,2,3]

(L은 리스트 변수명)
|문법|설명| 
|-|-|
|L.insert(i,x)| 리스트 인덱스 i에 x 삽입|
|L.remove(x)|리스트 첫번째 x를 제거. 존재하지 않으면 ValueError|
|L.pop()|리스트 마지막 반환 후 제거|
|L.pop(i)|리스트 인덱스 i에 있는 항목을 반환 후 제거|
|L.index(x)|x의 인덱스 번호를 반환|
|L.index(x ,start, end)|리스트 첫번째 x `값`(리스트 아님)를 반환|
|L.reverse()|리스트를 역순으로 뒤집음|
|L.sort()|리스트 오름차순으로 정렬|
|L.count(x)|리스트에서 x가 몇개 존재하는지 갯수를 반환|
|L.append(x)|리스트에 값 추가|
|L.extend(m)|기존 리스트에 새로운 원소를 추가|

<br>

```python
cafe = ['Dante', 'Starbucks']


cafe.append('Megacoffee')
#['Dante', 'Starbucks','Megacoffee']

cafe.extend(['Megacoffee', 'Ediya'])
#['Dante', 'Starbucks','Megacoffee','Ediya']

cafe.insert(0, '시작')
#['시작','Dante', 'Starbucks']

cafe.insert(10000, '끝')
#['Dante', 'Starbucks', '끝']
# 10000자리에 온 숫자가 리스트 길이보다 큰 경우에는 리스트의 맨 끝에 '끝'이 온다.

cafe.remove('Dante')
# ['Starbucks']

cafe.pop()
#['Dante']

cafe.pop(0)
#['Starbucks']

cafe.clear()
#[]

cafe.index('Dante')
# 0

numbers = [1,2,3,1,1]
numbers.count(1)
# 3

numbers = [3,2,5,1]
result = numbers.sort()
print(numbers, result) # [1, 2, 3, 5] None

numbers = [3,2,5,1]
result = sorted(numbers)
print(numbers, result) # [3,2,5,1] [1,2,3,5]
# numbers는 변경되지 않은 원본 리스트를 반환한다.

numbers = [3,2,5,1]
result = numbers.reverse()
print(numbers, result) # [1,5,2,3] None

```

