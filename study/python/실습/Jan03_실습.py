# 문제1
# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

# integer = int(input('정수를 입력하세요'))

# if integer > 0:
#     print('True')

# else:
#     print('False')

#"================================"

# 문제2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

# integer1= int(input('첫번째 정수를 입력하세요'))
# integer2= int(input('두번째 정수를 입력하세요'))

# if integer1 > integer2:
#     print(max(integer1, integer2))

# elif integer1 < integer2:
#     print(max(integer1, integer2))

# else:
#     print(False)

#"================================"

# 문제3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.

# integer = int(input('정수를 입력하세요'))

# if 1 < integer < 10:
#     print(True)

# else:
#     print(False)

#"================================"

# 문제4
#정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.

# integer = int(input('정수를 입력하세요'))

# if (integer > 0) & (integer %2 == 0):
#     print(True)

# else:
#     print(False)

#"================================"

# 문제5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.

# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

# integer = int(input('정수를 입력하세요'))


# if integer > 100:
#     print('에러')

# elif integer > 60:
#     print('합격')

# elif integer > 0:
#         print('불합격')

# else:
#     print('에러')

#"================================"

# 문제6 🎈
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# 힌트 : 문자열 역슬라이싱

# 방법1) reverse 이용하기 문자열 뒤집기

# chars = input('문자열을 입력하세요')

# chars_list = list(chars)
# # print(chars_list)

# chars_list.reverse()
# # print(chars_list)

# chars1 = ''.join(chars_list)
# print(chars1)

# 방법2)[::-1] 문자열 슬라이싱을 이용하여 문자열 뒤집기 ❌ 

# chars = input('문자열을 입력하세요')

# chars1 = chars[::1]
# chars2 = chars[::2]
# chars3 = chars[::-1]
# chars4 = chars[::-2]

# print(chars1)
# print(chars2)
# print(chars3)
# print(chars4)

#"================================"

# 문제7

# integer1= int(input('첫번째 정수를 입력하세요'))
# integer2= int(input('두번째 정수를 입력하세요'))



# if integer1 < integer < integer2:
#     print(integer)


#"================================"

# 문제8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.

# 두 값이 같으면 False를 출력하세요

#"================================"

# 문제9
# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.

# 입력 값이 1보다 작으면 False를 출력하세요.

#"================================"

# 문제10 🎀

# a = range(2,10)
# b = range(2,10)

# for i in a:
#     for j in b:
      
#         # print(f'{i} X {j} = i*j')
#         print(i, 'X', j, '=', i*j)



 