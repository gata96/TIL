import sys
input = sys.stdin.readline
N, M, V = map(int,input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

# M개의 간선 정보를 그래프에 반영하기
for _ in range(M):
    a, b = map(int,input().split())
    # a,b 입력을 받을 때 마다 graph에 양방향으로 1 표시하기
    graph[a][b] = True
    graph[b][a] = True
    