# KDT 2기 1월 3일 학습 내용

# %-format
```
name = 'kim'
score = 4.5

print('hello, %s' %name) -> s = 문자 name 대신 #hello, kim
print('내 성적은 %d' %score) -> d = 숫자 score 대신 #내성적은 4
print('내 성적은 %f' %score) -> f = 실수 scroe 대신 내성적은 4.500000
```

# f-string
```
name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}' )
```
> Hello, Kim! 성적은 4.5

<br>

```
pi = 3.141592
print(f'원주율은 `{pi:.3}`. 반지름이 2일때 원의 넓이는 {pi*4}')
```

> '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566968'

<br>

💟 pi:.3의 의미
- pi의 소수 셋째자리까지 표시

<br>


# True와 숫자의 계산

```
print(True + 3) #4
print(5.0 + 3) #8.0
print(3+5+4j) #(8+4j)
```

> print(True + 3) #4

> print(5.0 + 3) #8.0

> print(3+5+4j) #(8+4j)

<br>


# 문자와 실수, 정수의 계산

1. 문자 + 실수 -> ❌
```
'3' +4
```
> TypeError: can only concatenate str (not "int") to str
> 문자는 문자끼리, 숫자는 숫자끼리 합칠 수 있다.

<br>


2. int(문자) + 정수 -> ⭕
```
print(int('3') +4)
```
> #7

<br>


3. int(문자) + 정수 -> ❌
```
print(int('3.5') +4)
```
> ValueError: invalid literal for int() with base 10: '3.5'
> int(소수점)은 문제 없지만 str문자형을 int로 묶으면, int가 str를 감싸줄수 없기 때문에 에러가 발생한다.
> 해결방법: str -> float -> int

<br>


4. float(문자) + 정수
```
print(float('3.5') +4)
```
> #7.5

<br>

# if문 구조
```
if <표현식>:
    <Run here>
else: 
    <or not, Run here>
```

```
a = -10
if a >= 0:
    print('양수')  
else:
    print('음수')
print(a)
```
> 음수 -10

<br>


# 조건문을 이용해서 변수 num의 홀짝수 구분하기
### num은 사용자로부터 입력 받기
```
num = int(input('입력해주세요 > '))

if num % 2 == 0:
    print('짝수')
else:
    print('홀수')
```

<br>

# 조건문이 여러 개 일때

```
if <표현식>:
    <code block>:
elif <표현식>:
    <code block>:
elif <표현식>:
    <code block>:
else:
    <code block>:
```

<br>


### <예제>
미세먼지 농도에 따른 등급

💦내가 작성했던 코드
```
dust = int (input('입력'))

if dust<= 30:
    print('좋음')
if 30< dust <= 80:
    print('보통')
if 80< dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')
print('미세먼지 확인 완료')
```
> 더 간결하고 좋은 코드가 없을까? 🤔

💯Good code!
```
dust = int (input('입력'))

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

print('미세먼지 확인 완료')
```
> 첫번째 예시처럼 `30< dust <= 80` 식으로 작성할 필요가 없다!

<br>

# 이중 if문 (들여쓰기 유의하자)

```
if <표현식>:
    <code block>:
    if <표현식>:
        <code block>:
else:
    <code block>:
```
<br>

### <예제>
이중 if문을 활용해서 dust 값이 300이 넘는 경우 '실외활동을 자제하세요'를 출력, 음수인 경우 '값이 잘못되었습니다' 출력.

```
dust = int (input('입력'))

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('실외활동을 자제하세요')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('값이 잘못되었습니다')
    else:
        print('좋음')

print('미세먼지 확인 완료')
```
> if 안에 if, else 안에 if와 else

<br>

# range
- range(n) : 0부터 n-1 까지  

- range(n,m) : n부터 m-1 까지  

- range(n,m,s) : n부터 m-1까지 s만큼 증가

```
range(4)
```
> range(0,4)

<br>


```
list(range(4))
```
> [0,1,2,3,]

<br>


```
type(range(4))
```
> <class 'range'> : type이 range그 자체이다.

<br>


```
list(range(1,5)))
```
> [1,2,3,4]

<br>


```
list(range(1,5,2))
```
> [1,3]

<br>


```
list(range(6,1,-1))
```
> [6,5,4,3,2]

<br>


```
list(range(6,1,1))
```
> []
> 6에서 1까지 감소해야하는데, 1만큼 증가하라고 했으니까 말이 안됨. 그래서 텅빈 list로 결과를 뱉어버림.

<br>

# for문
- 처음부터 끝까지 순회하기 때문에 별도의 종료 조건이 필요없다.

```
for <변수명> in <객체>:
    <code block>
```
```
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
```
>apple
>>mango
>>>banana
>>>>끝

<br>


### <예제>
사용자가 입력한 문자를 한글자씩 세로로 출력하기

```
chars = input()

for char in chars:
    print(char)
```
> 사용자가 입력한 값(Hello)이 변수 chars에 할당된다. Hello를 차근차근 앞에서 부터(for) 세로로 뱉어나가는 중(print).

> H
>>e
>>>l
>>>>l
>>>>>o

<br>


### 예제 (✨)

range활용해서 세로로 한글자씩 출력하기
```
chars = input() #gata
print(len(chars)) #4
print(range(len(chars))) #range(0,4)
print(range(4)) #range(0,4)
```
```
chars = input()
range(len(chars))
for idx in range(len(chars)): 
     print(chars[idx])
```

>range(chars) -> ❌ 
>range(문자) 불가능. 중간 단계에사 len 거쳐야한다.

<br>


```
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
```
> 1
>>3
>>>5

> for문이 continue를 만나면 print(i)가 실행되지 않고 바로 다음 반복을 시행.

<br>


```
for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다')
```
> #b

<br>


```
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다')
```
> #b가 없습니다.