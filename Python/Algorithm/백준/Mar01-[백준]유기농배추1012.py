import sys
sys.setrecursionlimit(10**6) # 재귀 함수 한도 늘려주기
input = sys.stdin.readline
MAX = 50 + 10 # 최댓값

dirR = [1, -1, 0, 0] # 하, 상, 오, 왼
dirC = [0, 0, 1, -1]


def dfs(y,x):
    global visited
    visited[y][x] = True
    for dirIdx in range(4):
        # idx 각각을 돌면서 현재 위치에서 이 값들을 더해줘서, 내 기준으로 부터 상하좌우를 다 돌 수 있음.
        newY = y + dirR[dirIdx] 
        newX = x + dirC[dirIdx]
        if graph[newY][newX] and not visited[newY][newX]: # 새로운 위치에 배추가 있는지와 방문한 적이 없는 배추추
            dfs(newY, newX) # 맨 처음은 1,1에서 시작하고, 상하좌우를 탐색하면서 배추가 있고, 아직 방문하지 않았다면, 다음곳으로 가겠다.

# 0. 입력 및 초기화
T = int(input()) # test case
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로,세로길이 , 배추 개수
    graph = [[False] * MAX for _ in range(MAX)] # 이차원 배열
    visited = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프에 배추 위치 정보 입력
    for _ in range(K):
        x, y = map(int,input().split()) # x, y 정보 입력 받기
        graph[y+1][x+1] = True # 0,0 base가 아닌 1,1 base로
    
    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0 # 지렁이 수
    for i in range(1,N+1): # 이차워 배열 돌기
        for j in range(1,M+1):
            if graph[i][j] and not visited[i][j]: # 그래프 상에 배추가 있고, 방문하지 않았다면
                dfs(i,j) # dfs를 수행하라
                answer += 1
    print(answer)
        
        
        




     