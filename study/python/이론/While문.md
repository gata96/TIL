# While

> '내가 피곤하면' 쌍화탕을 계속 줘
- while문은 for문과 달리 `조건`이 중요하다. 조건을 만족해야 돌아가기 때문이다. 
- 때문에 조건을 만족하는 한 무한 루프할 가능성이 있어 종료조건이 반드시 필요하다.

```python
while <표현식>:
    #code block
```
```python
a = 0
while a < 5:
    print(a)
    a+=1

print('끝')

# """
# 0
# 1
# 2
# 3
# 4
# 끝
# """
```
<br>

## for문

```python
target = int(input())
total = 0

for element in range(1,target+1):
    total += element

print(total)
```

## while문 (같은 문제)

```python
target = int(input())
n = 0
total = 0

while target >= n:
    total += n
    n += 1

print(total)

```
