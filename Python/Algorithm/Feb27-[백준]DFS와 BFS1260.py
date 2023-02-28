import sys

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    
def bfs():
    global q, visited
    while q: # q에 값이 있을 때 까지 반복 실행
        cur = q.pop(0) # 가장 앞에 있는 수 뽑아서 cur에 넣기
        visited[cur] = True # True 표시
        print(cur, end = ' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)



# 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int,input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

# 1. graph에 정보 입력
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(V) # 노드V부터 dfs 실행
print() # 줄바꿈

# 3. bfs
visited = [False] * (N+1) # visited 초기화
q = [V] # 첫번째 V =1을 q에 넣고 시작
bfs()