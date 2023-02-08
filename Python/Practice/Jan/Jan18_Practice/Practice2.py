# 1. 시험성적

score = int(input())
if score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif score >= 70:
  print('C')
elif score >= 60:
  print('D')
else:
  print('F')


# 2. 단어 뒤집기

T = int(input())

for t in range(1, T+1):
  saying = input().split() # == split(' ')  # == saying = list(input().split()) # list

  for say in saying:
    print(say[::-1], end = ' ')



# 3. 열 개씩 끊어 출력하기

saying = input()
N = len(saying)
for i in range(0,N,10):
  print(saying[i:i+10])


# 4. 나무 조각
num = list(map(int,input().split()))


while True:
  for i in range(4):
    if num[i] > num[i+1]:
      num[i], num[i+1] = num[i+1], num[i]
      print(*num)

  if num == [1, 2, 3, 4, 5]:
    break


nums = list(map(int, input().split()))
index = 0


'''
하드 코딩

while True:
  if num[0]>num[1]:
    num[0], num[1] = num[1], num[0]
    print(num)

  elif num[1]>num[2]:
    num[1], num[2] = num[2], num[1]
    print(num)

  elif num[2]>num[3]:
    num[2], num[3] = num[3], num[2]
    print(num)

  elif num[3]>num[4]:
    num[3], num[4] = num[4], num[3]
    print(num)
    
  elif num == [1,2,3,4,5]:
    break

'''

  
    
  