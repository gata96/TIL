# KDT 2기 2023년 1월 4일 학습 내용

# 함수

## 사용자 함수
- 구현되어 있는 함수가 없는 경우, 내가 직접 함수를 작성 할 수 있다.

```python
def function_name
    #code block
    return returning_value
```
<br>

## [내장함수](https://docs.python.org/ko/3/library/functions.html)

## import mate
- sum
- len
- pow
- sqrt

<br>

## import statistics
- pstdev (표준편차)

<br>

### 함수 `sum`을 이용하면 for문이나 while문과 달리, 다음과 같이 한줄로 표현할 수 있다. 

```python
# sum

print(sum(range(1, int(input())+1)))

```
``` python

# for문
target = int(input())
total = 0

for element in range(1,target+1):
    total += element

print(total)
```

```python
# while문

target = int(input())
n = 0
total = 0

while target >= n:
    total += n
    n += 1

print(total)
```


## print (*objects)
### *objects : *은 여러 값을 무한하게 받을 수 있다는 뜻.
```python
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')
```

``` python
print('hi', 'hello', sep='!')
```
> hi!hello
> 키워드 sep=' '는 기본값이 space이다. !가 space자리를 대신하게 된다.

```python
# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 space 
# end='\n' : end라는 키워드는 기본 값이 enter
# end=' ' : 기본 값이 가로로 붙이기 & 띄어쓰기
print('hi', end=' ')
print('hello')

#hi hello
```

<br>

## 함수의 반환 값(return)

```python
# print 함수는 반환 값이 없다. 
print(print('hi')) # None

# sum 함수는 합을 반환한다. 
print(sum([1, 2, 3])) # 6


a = 5
result = print(a)
print(result)
```

<br>

print(p)

<br>

## len(s)
- 길이 

```python
numbers = [10, 20, 5]

# 길이?
cnt = 0 
for number in numbers:
    cnt += 1 
print(cnt)

# 함수!
print(len(numbers))
```

<br>

## sum(숫자, start = 0)
- 왼쪽에서 오른쪽으로 합한 합계
- 문자열은 올 수 없다

<br>

## max ()
- 더 큰 숫자 반환

```python
numbers = [10, 20, 5]
print(max(numbers))
print(max(1, 5, 7))
```

<br>

## min ()
- 더 작은 숫자 반환

<br>

## sorted ()
- 오름차순

```python
a = [10, 20, 5]
print(sorted(a))
```

<br>

## abs ()
- 절댓값
- 인자가 복소수면 그 크기를 반환

<br>

## divmod(a, b)
- 두 수의 몫과 나머지

<br>

## pow(base, exp, mod = None)
- base의 exp 거듭제곱
- mod가 있는 경우, base의 exp 거듭제곱의 모듈로 mod를 반환

<br>

## round(number, ndigit = None)
- number을 반올림
- ndigit가 생략되거나 None이면, 입력에 가장 가까운 정수를 반환

<br>

## bin(x)
- 정수를 "0b"접두사가 붙은 이진 문자열로 반환

<br>

## hex(x)
- 정수를 "0x"접두사가 붙은 16진수 문자열로 반환

<br>

## oct(x)
- 정수를 "0o"접두사가 붙은 8진수 문자열로 반환

<br>

## ord(c)
- 유니코드 문자 c에 대응되는 유니코드 숫자로 반환

<br>

## chr(i)
- 유니코드 숫자가 정수 i에 대응되는 문자를 반환
<br>

```python
print(ord('a'))
print(chr(97))
```

<br>

# map

```python
map(function, iterable)
```

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)을 적용하고, 그 결과를 map object로 반환

```python
numbers = ['1', '2', '3']
result = 0
for number in numbers:
    result += int(number)
print(result)
```
```python
numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)
```
```python
# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))
```
```python
a = input()
print(a) # '2 5'
# 원하는 것은 숫자 2와 숫자 5

# 1. 문자열을 각각 쪼갠 요소를 가진 리스트로 변환 -> .split()
b = a.split()
print(b) # ['2', '5']

# 2. 각 요소를 숫자로 변환 -> map()
c = map(int, b)
print(c) # map 

# 3. 각각 변수에 저장
d, e = list(c) # list(c)가 [2, 5]
print(d, e) # 각각 2, 5
```
```python
# # 2 5
# d, e = map(int, input().split())
# print(d, e)
# # 2 5 7
# d, e, f = map(int, input().split())
# print(d, e, f)


# 결론
numbers = list(map(int, input().split()))
print(numbers)
d = numbers[0]
e = numbers[1]
```


