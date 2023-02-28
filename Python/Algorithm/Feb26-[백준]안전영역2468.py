'''
1.아이디어
- 주어진 N보다 큰 값을 찾고 cnt1씩 해준다.
- 방문하지 않은 곳은 False, 이미 방문한 곳은 True 처리

2. 시간복잡도
O(V+E)
V = N* N = 100 * 100 = 1만
E = 4V = 4만
V+E = 5만 < 2억 (=1초)

3. 자료구조
그래프: 전체 지도 필요, 이차원 배열 int[][]
방문여부: bool[][]
queue: BFS에서 사용
'''


import sys
input = sys.stdin.readline 

from collections import depue # 시간절약
def bfs(si,sj,h):
    q = deque()
    q.append((si,sj))
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)): # 상하좌우
            ni,nj = ci+di, ci+dj
            if 0<=ni<N and 0<nj<N and chk[ni][nj] == False and map[ni][nj]>h:
                q.append((ni,nj))
                chk[ni][nj] = True


def solve(h): # h 높이에 대해 잠기지 않는 영역 개수를 리턴
    cnt = 0
    for j in range(N):
        for i in range(N):
        # 값이 h보다 크면서 방문하지 않은곳 탐색
            if map[j][i] > h and chk[j][i] == False:
                bfs(i,j,h)
                cnt += 1
    return cnt
# h높이 기준으로 방문하지 않았고 그보다 큰 높이가 있으면 bfs로 돌려줌


N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]
chk= [[False] * N for _ in range(N)]

ans = 0
for h in range(100): # 물 높이 0~99 까지 지정
    ans = max(ans,solve(h))