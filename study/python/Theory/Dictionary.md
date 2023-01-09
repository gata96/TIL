# KDT 2기 2023년 1월 5일 학습 내용

# 1. 딕셔너리(Dictionary)란?

- 딕셔너리는 데이터를 key와 value가 대응되는 형태로 하나의 변수에 선언하는 자료형. 리스트, 튜플, 딕셔너리 같이 여러개의 값을 저장하는 자료형을 '컨테이너'라고 한다. 딕셔너리는 많이 사용되는 자료형 중 하나로, 데이터를 구조적으로 다룰 수 있다는 장점이 있다.

# 2. 딕셔너리 선언 방법과 주의사항

## `{key : value}` 형태로 선언
- 키와 값은 `:`로 구분 되고 value는 `,`로 구분된다.
- key(키)
    - key는 고유한 값이므로, `중복되는 key`는 사용할 수 없다. 이미 사용중인 key에 중복되는 key를 설정하면, 그 전의 key는 무시된다. 그 이유는 딕셔너리는 key를 중심으로 value를 추출해내는데, 동일한 key가 존재하면, 어떤 value를 추출해야하는지 알 수 없기 때문이다.
    - `(string, integer, float, boolean, tuple, range)` 사용 가능  
    - `(리스트와 딕셔너리 등 불가능)`
    
- value(값)
    - 어떠한 형태든 관계 없음(list, dictionary등)
    - 하나의 key에 value를 여러 개 넣을 수 있다.

```python
반 = {'A반':['짱구', '맹구'], 'B반':['철수, 유리']}
```
    

```python
a = {'A':'짱구', 'A':'철수'}
print(a)

# {A:'철수'}


students = {'오은정':75, 'Lucas':80}
students['오은정']

# 100
```
<br>

# 3. 딕셔너리 사용 방법

## 1) value 출력 방법 (3가지)  


### `변수[key]`
key를 이용해서 value 찾기

```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }

학교['1반'] 

#['오은정', '고멘시']
```

### `.get()`


```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }

학교.get('1반') 

#['오은정', '고멘시']
```

### 딕셔너리에 있는 모든 value 가져오기: `.values()`

```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }

학교.values()  

# dict_values([['오은정', '고멘시'], ['sabbar', 'minha']])
```

<br>

## 2) 딕셔너리에 있는 모든 key 가져오기: `.keys()`

```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }

학교.keys()  

# dict_keys(['1반', '2반'])
```

## 3) key와 value를 쌍으로 출력할 때: `.items() `
```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }
print(학교.items)

# dict_items([('1반', ['오은정', '고멘시']), ('2반', ['sabbar', 'minha'])])
```


### 예 - keys, values, items

```python
students = {'오은정':75, 'Lucas':80}

print(students.keys())
print(students.values())
print(students.items())

# dict_keys(['오은정', 'Lucas'])
# dict_values([75, 80])
# dict_items([('오은정', 75), ('Lucas', 80)])
```


## 4) 딕셔너리에 `key-value` 쌍을 추가 할 수 있고, 이미 해당하는 키가 있다면 기존 value 값이 변경된다.
## `변수[key] = value`

```python
students = {'오은정':75, 'Lucas':80}
students['오은정'] = 99
students['Meu Gato'] = 95

print(students['오은정']) # 99
print(students)  # {'오은정': 99, 'Lucas': 80, 'Meu Gato': 95}
```

## 5) 키 삭제: ` .pop` 또는 `del`
## `변수.pop('key')`
## `del 변수['key']`

```python
students = {'오은정':75, 'Lucas':80}
students.pop('Lucas')
print(students)

# {'오은정': 75}
```
```python
students = {'오은정':75, 'Lucas':80}
del students['Lucas']
print(students)

# {'오은정': 75}
```

## 6) values 수정
## `변수[key]=변경할 value`

```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }

학교['2반' = 'Meu']

print(학교)

# {'1반': ['오은정', '고멘시'], '2반': 'Meu'}
```

## 7) 딕셔너리에 해당 key 또는 value 가 있는지 확인
## `key in 변수` 또는 `value in 변수`
```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }
print('2반' in 학교)
# True

print('3반' in 학교)
# False

print('lucas' in 학교)
# False
```

## 8) 키가 없는 경우 : `KeyError` 발생

```python
students = {'오은정':75, 'Lucas':80}
students.pop('sabbar')

# KeyError: 'sabbar'
```
## 9) 딕셔너리 순회
- 딕셔너리는 key를 순회하며, key를 통해 값을 뱉는다.

```python
students = {'오은정':75, 'Lucas':80}

for name in students:
    print(name)

# 오은정
# Lucas
```
```python
students = {'오은정':75, 'Lucas':80}

for name in students:
    print(name, students[name])

# 오은정 75
# Lucas 80
```

## 10) 딕셔너리의 모든 값을 지우고 싶을 때: `.clear()`

```python
학교 = {'1반':['오은정', '고멘시'], '2반': ['sabbar', 'minha'] }
print(학교.clear())  # None
print(학교)          # {} 
