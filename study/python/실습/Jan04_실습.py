# 문제 1 🎈
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

# 단, abs() 함수는 사용하지 마세요.

number = int(input())

import math

def abs_aign(number):
    if number >= 0:
        return number
    else:
        return -number

print(number) # ->에러....

# ======================================

# 문제 2
# 정수만 저장한 리스트가 주어집니다.

# 리스트 요소의 개수를 출력하세요.

# 단, len() 함수는 사용하지 마세요.

number_list = [1, 2, 3, 4, 5]
print(len(number_list))
# --------------------------------------

number_list = []
print(len(number_list))

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
# --------------------------------------
number_list = [-1, -2, -3, -4, -5]
total = 0

for i in number_list:
    total +=i

print(total)

# ======================================
# 문제 4 🎈
# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 평균을 출력하세요.

# 단, len() / sum() 함수는 사용하지 마세요.

number_list = [2, 4, 6]
total = 0

for i in number_list:
    total += i

# print(total)

# for idx in number_list:
#     j += 1
#     print(j)


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

# print(total)
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

# 방법1)
number_list = [1, 3, 4, 2, 5]
number_list.sort(reverse= True)
number_list[0]
print(number_list[0])


#❓ for문을 이용해서 어떻게 구하지? 
# 방법2)
number_list = [1, 3, 4, 2, -1]

a = 0
for max in number_list:
    if a < max:
        a = max
    else:
        continue
print(a)


# 리스트.sort는 리스트 안의 원소들을 오름차순으로 정렬
# 리스트.sort(reverse = True) 는 리스트 안의 원소들을 내림차순으로 정렬

# 방법1)
number_list = [1, 1, 1]
number_list.sort(reverse= True)
number_list[0]
print(number_list[0])

# # =====================================

# # 문제 7

number_list = [1, 2, 3, 4, 5]
number_list.sort()
print(number_list[0])