# 코딩테스트 정복을 위한 데이터 구조와 알고리즘

- Array(배열)
- Linked List(연결리스트)
- Hash(해시)
- Stack(스택)
- Queue(큐)
- Priority Queue(우선순위 큐)
- Heap(힙)
- Tree(트리)
- Graph(**그래프**)

[기본]
완전탐색, 재귀, 시뮬레이션, 그리디

[심화]
DFS, BFS, 백트래킹, 이진탐색, DP, 다익스트라, 크루스칼, 프림

# 1. Stack(스택)

뷔페에서 제일 위에 있는 접시를 꺼내듯이, 가장 마지막에 들어온 데이터가 가장 먼저 나가는 방식

## List를 stack으로 이용
  stack = []

## 스택에서는 append와 pop을 이용하면 된다.
append : 가장 뒤에 값을 넣는다.
pop : 가장 마지막 값을 꺼낸다.

```python
stack.append(5)
stack.append(3)
stack.append(2)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # [5,2,3,1]
print(stack[::-1]) # [1,3,2,5]
```

## 언제 사용할까?
구글 => 네이버 => 유튜브에서 `뒤로가기` 누르면 이전 웹사이트로 이동하거나, 문서작업시 Ctrl + z로 뒤로가기를 하듯이, 리스트에서 pop을 해서 이전의 데이터를 불러온다.

## 스택이 많이 쓰이는 알고리즘 유형
- 괄호 매칭
- 재귀 함수 : 스택 대신 많이 사용된다.
- 백트래킹
- DFS

## 재귀 함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- 재귀 함수는 출력 횟수에 제한이 있기 때문에 어느 정도 출력하다가 초과 에러 메시지가 출력됨
- 재귀 함수에서는 종료 조건을 반드시 명시해야한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출 될 수 있다.
- 예제
  - '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력

```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()
recursive_function()

# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 재귀 함수를 호출합니다.
# 에러 출력
```
- 종료 조건을 포함한 재귀함수 예제
```python
def recursive_function(i):
    # 100번째 호출을 했을 때 종료될 수 있도록 종료 조건 명시
    if i == 100:
        return
    print(f'{i}번째 재귀 함수에서 {i+1}번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(f'{i}번째 재귀 함수를 종료합니다.')

recursive_function(1)
```

# 2. 큐(Queue)
- 입구와 출구가 양 옆으로 모두 뚫려있다.
- 데이터가 오른쪽에서 들어오고(append), 가장 오래기다린 데이터가 왼쪽으로 나간다(popleft).
- 대기줄 : 가장 오래 기다린 사람이 가장 먼저 나간다.
    가장 오래 기다린 사람을 꺼내는 것 : Dequeue = pop(0)
    맨 뒷 줄에 새로운 사람을 넣는 것 : Enqueue = append
- deque을 사용함으로써 큐를 구현하고 시간도 절약할 수 있다.
  
```python
from collections import deque

# queue(큐) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # deque[3,7,1,4]
queue.reverse() # 역순
print(queue) # deque[4,1,7,3]
```





## 언제 큐를 사용할까?
대기열 필요할때
- BTS 티켓팅 할 때
- 프로세스 관리(데이터 버퍼)
- 클라이언트/서버(Message Queue)