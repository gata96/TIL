import sys


# 0. 입력 및 초기화
M, N, K = map(int, input().split()) # 가로,세로길이 , 배추 개수
graph = [[False] * (N+1) for _ in range(M+1)]
visited = [False] * (N+1)



for _ in range(K):
    X, Y = map(int,input().split())
    