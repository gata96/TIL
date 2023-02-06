## 지능형 기차
total = 0
lst = []
while True:
    minus, plus = list(map(int,input().split()))
    total += plus - minus
    lst.append(total)
    if plus == 0:
        break
print(max(lst))

## 행복한지 슬픈지
import sys
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline 

say = input()
cnt_h = say.count(':-)')
cnt_s = say.count(':-(')

if cnt_h > cnt_s:
    print('happy')
elif cnt_h < cnt_s:
    print('sad')
elif cnt_s == cnt_h == 0:
    print('none')
elif cnt_s == cnt_h:
    print('unsure')


## 바이러스
# 입력을 받아 인접리스트 생성
n = int(input()) # 컴퓨터 개수
m = int(input()) # 연결된 선 개수

# graph = []
# lst = []
# for _ in range(n+1): # 빈 리스트까지 만들어야 하므로 컴퓨터개수 + 1 = 8개 반복
#     graph.append(lst)

# 단계 0. 빈 인접리스트와 방문기록지 만들기
graph = [[] for _ in range(n+1)] # graph는 n+1만큼 빈 리스트를 생성. n+1인 이유는 1번 컴퓨터를 1번 인덱스로 쓰기위
visited = [False] * (n) # 방문기록지

# 단계 1. 입력값을 받아 인접리스트 만들기
for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2) # v1에 v2 넣고
    graph[v2].append(v1) # v2에 v1 넣어서 서로 쌍방으로 연결되어있도록 함.

def dfs(v):
    stack = [v] # stack 만들고, 방문할 컴퓨터 stack에 넣기
    visited[v] = True # 방문한 컴퓨터를 True 표시
    while stack: # stack에 값이 존재할 때까지 반복한다.
        num = stack.pop() # stack에서 1꺼내기
       
        for i in graph[num]: # 1번 컴퓨터와 인접한 컴퓨터를 순회
            if not visited[i]: # 아직 방문하지 않았다면, 즉 False라면
                visited[i] = True # 방문기록지에서 False -> True로 바꾼후 
                stack.append(i) # 1번 컴퓨터의 child node를 stack에 담기
dfs(1) # 1번 컴퓨터 부터 시작
print(sum(visited)-1)


