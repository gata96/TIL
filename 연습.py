1. 아이디어
- 2중 for문 => 값 1 찾기 && 방문X 곳을 찾기 => BFS로 해결
- BFS 돌면서 그림 개수 +1, 최댓값을 갱




import sys
input = sys.stdin.readline

n,m = map(int,input().split())
# 그래프 전체 지도: 이중for문
map = [list(map(int,input().split())) for _ in range(n)] 

# 방문
chk = [[False] * m for _ in range(n)]