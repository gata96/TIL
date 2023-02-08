# 문제1
# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

integer = int(input('정수를 입력하세요'))

if integer > 0:
    print('True')

else:
    print('False')

#===================================================================

# 문제2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

# 방법1)

integer1= int(input('첫번째 정수를 입력하세요'))
integer2= int(input('두번째 정수를 입력하세요'))


if integer1 > integer2:
    print(max(integer1, integer2)) 📌 # print(ineger1)으로 더 간결하게 만들 수 있다.

elif integer1 < integer2:
    print(max(integer1, integer2)) 📌 # print(ineger2)으로 더 간결하게 만들 수 있다.

else:
    print(False)

#-------------------------------------------------------------------------
#방법2)

number1 = int(input("첫 번째 정수를 입력하세요 > "))
number2 = int(input("두 번째 정수를 입력하세요 > "))

if number1 == number2:  📌 # elif, else가 아닌 모두 if로 표현할 수 있다.
    print(False)
if number1 > number2:
    print(number1)
if number1 < number2:
    print(number2)

#===================================================================

# 문제3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.

integer = int(input('정수를 입력하세요'))

if 1 < integer < 10:
    print(True)

else:
    print(False)

#===================================================================

# 문제4
#정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

integer = int(input('정수를 입력하세요'))

if (integer > 0) & (integer %2 == 0): 
    print(True)

else:
    print(False)

# 📌 더 좋은 코드로 수정

integer = int(input('정수를 입력하세요'))

if integer > 0:
    if integer %2 == 0:
        print(True)
    else:
        print(False)

else:
    print(False)

#===================================================================

# 문제5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

integer = int(input('정수를 입력하세요'))


if integer > 100:
    print('에러')

elif integer > 60:
    print('합격')

elif integer > 0:
        print('불합격')

else:
    print('에러')


# 📌 더 좋은 코드로 수정

if integer > 100 or integer < 0:
    print('에러')

else:
    if integer >= 60:
        print('합격')
    else:
        print('불합격')

#===================================================================

# 문제6 🔅
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# 힌트 : 문자열 역슬라이싱

# 방법1) reverse 이용하기 문자열 뒤집기
chars = input('문자열을 입력하세요') # input()으로 문자열 입력 받기
chars_list = list(chars) # 리스트에 담기
chars_list.reverse() # 리스트내 원소들을 반대 순으로 나열
chars1 = ''.join(chars_list) # 리스트를 문자열로 바꾸기
print(chars1)

# 에러
chars = input("문자열을 입력하세요 > ")
chars_list = list(string)
chars_oppo = chars_list.reverse() #❌에러 => 📌 chars_oppo변수에 담지 말것. 
result = ''.join(chars_oppo)               # 📌 다이렉트로 chars_list를 쓸 것.


# 방법2)[::-1] 문자열 슬라이싱을 이용하여 문자열 뒤집기 ❌ 

chars = input('문자열을 입력하세요')

for element in chars[::-1]: # [::-1]을 이용하면 문자열을 리스트로 넣을 필요 없이 바로 문자열을 뒤집을 수 있다.
    print(element)

#===================================================================

# 문제7
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요.

number1 = int(input('첫번째 정수를 입력하세요'))
number2 = int(input('두번째 정수를 입력하세요')) # 📌number1과 2는 입력 순서가 존재

if number1 < number2:
    for element in range(number1 + 1, number2):
        print(element)

elif number1 > number2:
    for element in range(number2 + 1, number1):
        print(element)

else:
    print(False)

#===================================================================

# 문제8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

# 두 값이 같으면 False를 출력하세요.

number1 = int(input('정수를 입력하세요'))
number2 = int(input('정수를 입력하세요'))

if number1 < number2:
    for element in range(number2 - 1, number1, -1):
        print(element)

elif number1 > number2:
    for element in range(number1-1, number2, -1):
        print(element, end= ' ')

else:
    print(False)

#===================================================================

# 문제9
# 정수 한 개를 입력 받고, 1부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

number = int(input("정수를 입력하세요 >"))

if 1 <= number:
    for element in range(1,number):
        if element %2 == 1:
            print(element)

else:
    print(False)

#===================================================================

# 문제10 구구단 출력하기 

for i in range(2,10):
    for j in range(2,10):
      
        print(f'{i} X {j} = {i*j}')





