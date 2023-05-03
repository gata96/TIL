# 학습 목표
# 딕셔너리 활용 코드를 읽고, 출력 결과를 예측할 수 있다.
# 딕셔너리 순회 작동 방식을 이해하고, 순회 결과를 예측할 수 있다.
# 에러가 발생했을 때 에러의 원인을 설명할 수 있다.
#=====================================================================
# 예제 1

dict_variable = {} # {} 딕셔너리 만들기
dict_variable['이름'] = '정우영'  # 딕셔너리명['key'] = 'value'
dict_variable['생년월일'] = '19000101'
dict_variable['회사'] = '하이퍼그로스'

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스
#=====================================================================

# 예제 2

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"


print(dict_variable["a"]) # A 
print(dict_variable["D"]) # d 
print(dict_variable["b"]) # KeyError: 'b'

#📌 dict_variable["B"] #key 값인 B가오면 결과가 b로 에러없이 나온다.
#=====================================================================

# 예제 3

dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"]) # 2000
print(dict_variable["banana"] ) # 4000
print(dict_variable["apple"] + dict_variable["banana"]) # 6000
#=====================================================================

# 예제 4

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key]) 

# """
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# """
#=====================================================================

# 예제 5

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

# """
# 이름 정우영
# 생년월일 19000101
# 회사 하이퍼그로스
# """
#=====================================================================

# 예제 6

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

# in의 의미
# x in s : s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False

#=====================================================================

# 예제 7

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # 딕셔너리에 '거주지'가 없으면 ket를 '거주지'로, value를 '서울특별시'로 해서 딕셔너리에 추가하세요.
    
print(dict_variable) 
# {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}
#=====================================================================


# 예제 8

list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# """
# 리스트 원소는 3개 밖에 없는데, index = 3은 4번째 원소를 의미하기 때문
# """
#=====================================================================

# 예제 9

try:
    number = 1
    if number == 1:
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

# """
# 조건문의 마지막에 ':' 을 붙히지 않았기 때문
# """ 
#=====================================================================

# 예제 10

n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100


