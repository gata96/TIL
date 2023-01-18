# # #1
# # '''
# # 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.'''
# # score = int(input())

# # if score >= 90:
# #   print('A')
# # elif score >= 80:
# #   print('B')
# # elif score >= 70:
# #   print('C')
# # elif score >= 60:
# #   print('D')
# # else:
# #   print('F')

# # #2 -> enter
# # '''
# # 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.
# # 2
# # I am happy today
# # We want to win the first prize
# # '''
# T = int(input())

# for t in range(1, T+1):
#   saying = input().split() # == split(' ')

#   for say in saying:
#     print(say[::-1], end = ' ')

#  # == saying = list(input().split()) # list

# # #3
# # '''
# # 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

# # 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
# # BaekjoonOn
# # lineJudge
# # '''
# saying = input()
# N = len(saying)
# for i in range(0,N,10):
#   print(saying[i:i+10])

# # # 4
# # '''
# # 동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.

# # 동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.

# # 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# # 두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# # 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# # 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# # 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
# # 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.'''

num = list(map(int,input().split()))


while True:
  for i in range(4):
    if num[i] > num[i+1]:
      num[i], num[i+1] = num[i+1], num[i]
      print(*num)

  if num == [1, 2, 3, 4, 5]:
    break


# nums = list(map(int, input().split()))
# index = 0



# # '''
# # 하드 코딩

# while True:
#   if num[0]>num[1]:
#     num[0], num[1] = num[1], num[0]
#     print(num)

#   elif num[1]>num[2]:
#     num[1], num[2] = num[2], num[1]
#     print(num)

#   elif num[2]>num[3]:
#     num[2], num[3] = num[3], num[2]
#     print(num)

#   elif num[3]>num[4]:
#     num[3], num[4] = num[4], num[3]
#     print(num)
    
#   elif num == [1,2,3,4,5]:
#     break

# # '''

  
    
  