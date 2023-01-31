# 별찍기
N = int(input())
for _ in range(N,0,-1):
    print(("*"*_).rjust(N))

# 대푯값
#  from sys import stdin as s
import sys
import statistics
# sys.stdin = open('input.txt', 'rt')
input = sys.stdin.readline

lst = []
for i in range(10):
    N = int(input().strip())
    lst.append(N)
print(statistics.mean(lst))
print(statistics.mode(lst))

# 세로읽기
import itertools # 2중 리스트를 1차원 으로 풀기
matrix = [input().strip() for i in range(5)]

v_matrix = list(zip(*matrix)) # 세로 읽기
print(*v_matrix)
l_list = list(itertools.chain(*v_matrix))
print(l_list)
# print(*l_list)

# 박스

for _ in range(int(input())): # 반복할 횟수
    n, m = map(int,input().split()) # 몇행 몇열
    grid = [input().split() for _ in range(n)] # 전체 리스트 생성
    total = 0

    for j in range(m): # 열부터 세로로 훑기
        cnt = 0       
        for i in range(n-1,-1,-1): # 맨 뒤 리스트부터 거꾸로 탐색
            if grid[i][j] == '1':
                total += cnt
            else:
                cnt += 1 # 인덱스 값을 찾는 대신, 0이 나올 때마다 1씩 임시 카운트 값(cnt)을 추가해주면 된다.
    print(total)


