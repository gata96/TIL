# # # 공

# # import sys
# # sys.stdin = open('input.txt','rt')
# # input = sys.stdin.readline

# N = int(input())

# cups = [1,2,3] 
# for _ in range(N):
#     x, y = map(int, input().split()) # 숫자 입력
    
#     xi = cups.index(x) # 입력 받은 숫자의 인덱스를 구해주기
#     yi = cups.index(y)

#     cups[xi], cups[yi] = cups[yi], cups[xi] # 인덱스를 이용해서 공의 위치를 바꿈
# print(cups[0]) # 공의 위치가 인덱스 0에 있으니까, 인덱스 0에 해당하는 숫자를 출력


# # # 콘테스트
# # # import sys
# # # sys.stdin = open('input.txt','rt')
# # # input = sys.stdin.readline

# W = []
# K = []
# for i in range(20):
#     score = int(input())    
#     if i < 10:
#         W.append(score)
#     else:
#         K.append(score)
    
#     W_sorted = sorted(W)
#     K_sorted = sorted(K)

# print(sum(W_sorted[-3:]),sum(K_sorted[-3:]))



# # # 오르막길

T = int(input()) # 측정할 수열 크기 
H = list(map(int,input().split())) # 측정한 길이를 H라는 리스트에 담아주기
dis = 0 # 오르막 높이를 임시로 저장할 변
lst = [] # 오르막길의 높이를 저장할 리스트

for i in range(T): #for문을 돌면서 앞 높이랑 뒤 높이랑 비교해서 
    if H[i-1] < H[i]: # 뒤 높이가 더 길면 
        dis += H[i]-H[i-1] # 뒤 높이 빼기 앞 높이
        # if i == T-1: # i==T-1이고 오르막길이라면 lst에 추가가 되지 않으므로
        #     lst.append(dis)
    else:
        lst.append(dis) # 오르막길이 아니라면 lst에 dis를 더해주고 dis를 0으로 초기화한다.
        dis = 0 

print(max(lst))

----
n = int(input())
li = list(map(int,input().split()))

li_t,t = [],0
for i in range(n-1):
    if li[i+1] > li[i]:
        t += (li[i+1] - li[i])
    else:
        li_t.append(t)
        t = 0
li_t.append(t)
---

n=int(input())

road=list(map(int,input().split()))

start=0 #새로운 수열 처음 위치 확인
uphill=[]

for i in range(n-1):
    
    if road[i]<road[i+1]:
        
        if i+1==n-1:
            uphill.append(road[i+1]-road[start])
    else:
        uphill.append(road[i]-road[start])
        start=i+1

print(max(uphill))
---

import sys

word = list(map(str, sys.stdin.readline().rstrip()))
list = []

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        first.reverse()
        second.reverse()
        third.reverse()

        list.append("".join(first + second + third))

    print(min(list))