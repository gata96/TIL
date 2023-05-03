# number = int(input())
# print(number)
# 2

# 공백으로 구분된 여러개의 정수 입력받기
# numbers = list(map(int,input().split()))
# print(numbers) 
#[2,5]
# print(*numbers)를 쓰면 리스트가 아닌 2 5가 나온다.
# unpacking

# for number in numbers:
#     print(number, end=' ')


# 공백으로 구분된 여러개의 단어 입력 받기
# string = input().split()
# print(string)
# [2, 5, 6, 9, 8]

# 공백으로 구분된 2개의 정수 입력 받기
# a, b = list(map(int,input().split()))
# print(a, b)
# 5 2

# 문제 1
# 5 출력받기
# number = int(input())
#============================================

# 문제 2
#  2 5 출력 받기
# a, b = list(map(int, input().split()))
# print(a, b)
# print(type(a)) # int
# print(type(b)) # int
#============================================

# 문제 3
#  1 2 3 출력받기
# a, b, c = list(map(int, input().split()))
# print(a, b, c)
# print(type(a b c)) # int
#============================================

# 문제 4
# word1 word2 word3 출력받기
# words = input().split()
# print(words)
# # ['word1', 'word2', 'word3']
# print(type(words)) #list

# print(*words)
# word1 word2 word3
# print(type(*words)) #str
#============================================

# 문제 5
# 1 2 3 4 5 출력받기

# numbers = list(map(int, input().split()))

# print(numbers)
# # [1, 2, 3, 4, 5]
# # list
# print(type(numbers))
#============================================

# 문제 6
# -10 10 출력받기

# a, b = list(map(int, input().split()))

# print(a, b)
# -10 10
#============================================

# 문제 7
# a b c d e 출력받기

# strings = input().split() #list

# print(strings) 
# ['a', 'b', 'c', 'd', 'e']
#============================================

# 문제 8
# 3 17 1 39 8 41 2 32 99 2 출력받기

# numbers = list(map(int, input().split()))

# print(numbers)
# [3, 17, 1, 39, 8, 41, 2, 32, 99, 2] 
#============================================

# 문제 9
# 1 4 0 10 2 3 9  출력받기

# numbers = list(map(int, input().split()))

# print(numbers)
# [1, 4, 0, 10, 2, 3, 9]