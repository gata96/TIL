# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 문자열 입력
# 문자열을 하나씩 훑어야한다 -> for(반복)
# element가 e를 만나면 리스트에 e를 담는다.

string = input('문자열을 입력하세요 > ')
string_list =[]

for element in string:
    if element == 'e':
        string_list.append(element)

print(len(string_list))

# 다른 방법 
string = input('문자열을 입력하세요 > ')
count = 0

for str in string:
    if str == 'e':
        count += 1
    
print(count)

#===================================================================
# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

# 단, count() 메서드는 사용하지마세요.

list = ['a','e','i','o','u','A','E','I','O','U']

string = input ('문자열을 입력하세요 > ')
count = 0
for str in string:
    if str in list: # 'in'사용
        count += 1

print(count)

## 다른 방법

count = 0
for str in string:
    if (
        str == 'a'
        or str == 'e'
        or str == 'i'
        or str == 'o'
        or str == 'u'
        or str == 'A'
        or str == 'E'
        or str == 'I'
        or str == 'O'
        or str == 'U'
    ):
        count += 1
print(count)

#===================================================================
# 문제 3
# 입력과 같은 딕셔너리 변수가 있을 때, 해당 인물의 나이를 출력하세요.

dict_variable = {
    "이름": "정우영",
    "생년": "20000101",
    "회사": "하이퍼그로스",
}

dict_variable['생년'] = 2000  # 생년을 2000(숫자)으로 바꾸기
print(dict_variable['생년']) # 2000

dict_variable['나이'] = 2024 - dict_variable['생년'] 
print(dict_variable['나이']) # 24


#-------------------------------------------

print(dict_variable['생년']) # 20000101
print(type(dict_variable['생년'])) # 20000101은 str(문자 타입)

result = (dict_variable['생년'])[0:4] # 문자열을 0번째부터 3번째까지의 문자열을 가져오기
print(result) # 2000 (문자타입)

#-------------------------------------------

#### 다른 접근(딕셔너리에 key와 value 추가)

dict_variable['나이'] = '24세'  # key는 '나이', value는 '24세'로 새로 추가
print('나이 :', dict_variable['나이']) # key가 나이인 value값을 찾고 싶다.

#===================================================================
# 문제 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

name = input('이름을 입력하세요 > ')
number = input('전화번호를 입력하세요 > ')
address = input('거주지를 입력하세요 > ')

dic = {'이름': name, 
        '전화번호': number, 
        '거주지':address
}

print(dic)

print(f'이름 : {name}')
print(f'전화번호 : {number}')
print(f'거주지 : {address}')

더 좋은 코드
for key, value in dic.items():
    print(f'{key} : {value}')

#===================================================================

# 문제 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.

# Hint : 딕셔너리 안에 딕셔너리를 넣을 수 있습니다.

name = input('이름을 입력하세요 > ')
number = input('전화번호를 입력하세요 > ')
email = input('이메일를 입력하세요 > ')
address = input('거주지를 입력하세요 > ')

dic = {
    name: {
        '전화번호': number, 
        '이메일': email, 
        '거주지': address
    }
}   # 딕셔너리 안에 딕셔너리를 넣을 수 있다.

print(dic)

#===================================================================


# 문제 6 (딕셔너리) 🎀
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

string = input("문자열을 입력하세요 > ")
dict_variable = {}
for char in string:
    if char in dict_variable.keys():
        dict_variable[char] += 1
    elif char not in dict_variable.keys():
        dict_variable[char] = 1

for key, value in dict_variable.items():
    print(key, value)

