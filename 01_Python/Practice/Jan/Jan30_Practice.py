# # 이상한 곱셈
import sys
input = sys.stdin.readline
A, B = input().split()
# print(type(A)) # str

A =list(map(int, A)) # int로 바꿔줌
B =list(map(int,B)) # int로 바꿔줌
print(sum(A)*sum(B))

# # 별 찍기
n = int(input())
for _ in range(1,n+1):
    print('*'*_)

# # 구구단
n = int(input())
for _ in range(1,10):
    print(f'{n} * {_} = {n*_}')

# # 나는 요리사
# # 5 X 4 행렬 만들기
# # 리스트 컴프리헨션으로 해보기
l_s = list(map(int, input().split()))
l_s = list(input().split())
print(type(l_s))
print(l_s)
l_s = [sum(list(map(int,input().split()))) for _ in range(5)]
print(l_s.index(max(l_s))+1, max(l_s))    

# # 직사각형 네개의 합집합의 면적 구하기
import pprint
xy_list = [[0 for _ in range(1,101)] for _ in range(1,101)]
# pprint.pprint(xy_list)
for i in range(4):
    x1, y1, x2, y2 = list(map(int,input().split()))

arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for j in range(x1, x2):
        for k in range(y1, y2):
            if arr[k][j] == 0:
                arr[k][j] = 1
                cnt += 1
print(cnt)