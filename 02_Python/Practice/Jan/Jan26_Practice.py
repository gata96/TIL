
# 세탁소 사장 동혁
import sys
T = int(sys.stdin.readline)
num = [int(sys.stdin.readline) for t in range(T)]
dollar = [25,10,5,1]
changes = [0,0,0,0]

for i in range(4):
    changes[i] += num // dollar[i] 
    num %= dollar[i]

print(*changes)


# # 피시방 알바
import sys
input = sys.stdin.readline

cnt = int(input())
num1 = list(map(int, input().split()))
num2 = set(num1)

print(len(num1)-len(num2))

# # 제로

import sys
input = sys.stdin.readline
num_list = []
cnt = int(input())

for i in range(cnt):
    num = int(input())

    if num != 0:
        num_list.append(num)

    else:
        num_list.pop()
        
print(sum(num_list))

# # 카드 1

import sys
input = sys.stdin.readline

num = int(input()) # 7

num_list = list(range(1,num+1)) # [1,2,3,4,5,6,7]
trash_bin = []

while len(num_list) > 1: # while 에서는 ==사용 안됨
    trash_bin.append(num_list.pop(0)) # for문 없이 pop(인덱스)로 원소 선택할 수 있다
    num_list.append(num_list.pop(0))

print(*trash_bin, *num_list) # *는 리스트를 문자열로 바꿔준다.


# # 괄호

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    my_list = list(input())
    for j in my_list:
       if my_list.pop(0) == my_list.pop(-2):
        
