'''
1이 나왔을 때 주변의 1을 찾는 식으로
전체적으로 넓게 탐색: BFS 
2중 for문: 1이어야하고, 방문이 안되어있는 곳이어야함
1을 발견하면 그림 개수를 올려주고 최댓값을 찾는다.

1. 아이디어
2중 for문 : 값이 1 && 방문 X한 곳으로 BFS 돌기
BFS 돌면서 그림개수+1. 최댓값
2. 시간복잡도
O(V+E)
V: 점 개수 => n * m
E: 가지 개수 => V * 4(넉넉잡아 4, 동서남북으로 가지가 뻗어있으니까)
V+E = V + 4V = 5V = 5 * (500 * 500) = 약 100만 < 2억 (1초에 2억개 연산)

3. 자료구조
- 그래프: 전체 지도 필요 (이차원 배열) int[][]
- 방문 여부 : bool[][]
- Queue : BFS에서 사용
'''


import sys
input = sys.stdin.readline
# 3. 자료 구조
# map은 input을 int로 바꿔준다.
n,m = map(int,input().split())
# n행 만큼 지도를 만들어준다.
map = [list(map(int,input().split())) for _ in range(n)]
# 방문 여부 (가로m만큼 False 크기를 설정 한 후, n 행만큼 생성)
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1] #오 아 왼 위
dx = [1,0,-1,0]

def bfs(y,x):
    rs = 1 # 전체 크기
    q = [(y,x)]
    while q:
        ey, ex = q.pop() # q에서 하나씩 뽑아준다.
        for k in range(4): # 4방향으로 탐색
            ny = ey + dy[k] # 한칸씩 이동
            nx = ex + dx[k]
            #그림 넘어가면 안됨
            if 0 <= ny < n and 0 <= nx < m:
                 if map[ny][nx] == 1 and chk[ny][nx] == False:
                     rs += 1
                     chk[ny][nx] = True
                     q.append((ny,nx))
    return rs # 전체 크기 


# 그림 개수 
cnt = 0
# 최대 그림 크기
maxv = 0

# 이중 for문, 이차원 배열
# 보통 y를 먼저 돌고, x를 돈다.
for j in range(n):
    for i in range(m):
        # 값이 1이면서 방문하지 않은 곳을 돌기
        if map[j][i] == 1 and chk[j][i] == False:
            # 전체 그림 개수를 1개씩 올려주기
            cnt += 1
            # 방문 했던 곳은 방문처리해주기
            chk[j][i] = True
            # BFS로 그림의 크기를 구해주기
            # BFS한 결과로 최댓값 갱신
            maxv = max(maxv, bfs(j,i))

# 이중 for문이 끝나면 print
print(cnt)
print(maxv)