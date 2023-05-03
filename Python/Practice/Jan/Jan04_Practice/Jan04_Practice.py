# 문제 1
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

# 단, abs() 함수는 사용하지 마세요.

number = int(input('정수를 입력하세요 > '))


if number >= 0:
    print(number)

else:
    number_str = str(number) # 문자형으로 바꾼 후, 두번째 문자열 부터 추출
    print(number_str[1:])


#### 다른 방법 🎇
else:
    print(number *-1) # 음수에 -1 곱하기


# ======================================

# 문제 2
# 정수만 저장한 리스트가 주어집니다.

# 리스트 요소의 개수를 출력하세요.

# 단, len() 함수는 사용하지 마세요.

number_list = [1,2,3,4,5]

count = 0

for number in number_list:
    count = count + 1

print(count)


# ======================================

# 문제 3
# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 합을 출력하세요.

# 단, sum() 함수는 사용하지 마세요.

number_list = [1, 2, 3, 4, 5]
total = 0

for i in number_list:
    total +=i

print(total)


# # --------------------------------------
number_list = [-1, -2, -3, -4, -5]
total = 0

for i in number_list:
    total +=i

print(total)

# ======================================
# 문제 4 
# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 평균을 출력하세요.

# 단, len() / sum() 함수는 사용하지 마세요.

number_list = [2, 4, 6]
total = 0
count = 0

# 총 합
for i in number_list:
    total += i
print(total) 

# 총 개수
for number in number_list:
    count = count + 1
print(count)

print(total/count)

## 더 간단한 코드 🎇
number_list = [2, 4, 6]
total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total/count)


# print()는 NoneType 유형에 속하는 객체다.
# print(print(total)) : print 자체를 print하는 것의 결과는 None 이다.

# =====================================

# 문제 5

# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 곱을 출력하세요.

number_list = [1, 2, 3, 4, 5]
total = 1
for i in number_list:
    total *= i

print(total)
# # -------------------------------------

number_list = [-1, -2, 3]

total = 1
for i in number_list:
    total *= i

print(total)

# =====================================

#  문제 6
# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

# 단, max() 함수는 사용하지 마세요.

# 방법1) for문
number_list = [1, 2, 3, 4, 5]

for number in number_list:
    if number > number:
        number == number
print(number) 


# 방법2) sort

number_list = [1, 3, 4, 2, 5]
number_list.sort(reverse= True)
number_list[0]
print(number_list[0])

# 리스트.sort는 리스트 안의 원소들을 오름차순으로 정렬
# 리스트.sort(reverse = True) 는 리스트 안의 원소들을 내림차순으로 정렬

# # =====================================

# # 문제 7

# 방법1) for문

number_list = [5,5,5,2]
min_value = number_list[0] # list 원소의 가장 첫번째를 임의로 선정

for number in number_list:
    if min_value > number:
        min_value = number # = 와 ==의 차이
    
print(min_value)

# = 와 ==의 차이

# = 는 우변을 좌변에 할당한다
# == 는 두 객체의 값이 같은지를 비교하는 것. 
# 값이 같으면 True, 다르면 False를 출력한다.

# 방법2) sort()

number_list = [5,5,5,2]
number_list.sort() # 오름차순 정렬 꼭 '()' 쓰자
print(number_list[0])

