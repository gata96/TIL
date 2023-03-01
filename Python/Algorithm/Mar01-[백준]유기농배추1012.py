import sys
sys.setrecursionlimit(10**6) # 재귀 함수 한도 늘려주기
input = sys.stdin.readline
MAX = 50 + 10

# 0. 입력 및 초기화
T = int(input()) # test case
M, N, K = map(int, input().split()) # 가로,세로길이 , 배추 개수
graph = [[False] * (N+1) for _ in range(M+1)]
visited = [False] * (N+1)



for _ in range(K):
    X, Y = map(int,input().split())
    