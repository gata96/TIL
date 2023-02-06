# 코딩테스트 정복을 위한 데이터 구조와 알고리즘

- Array(배열)
- Linked List(연결리스트)
- Hash(해시)
- Stack(스택)
- Queue(큐)
- Priority Queue(우선순위 큐)
- Heap(힙)
- Tree(트리)
- Graph(그래프)

[기본]
완전탐색, 재귀, 시뮬레이션, 그리디

[심화]
DFS, BFS, 백트래킹, 이진탐색, DP, 다익스트라, 크루스칼, 프림

# 1. Stack(스택)

뷔페에서 제일 위에 있는 접시를 꺼내듯이, 가장 마지막에 들어온 데이터가 가장 먼저 나가는 방식의 LIFO(Last-in First-out, 후입선출)방식

push : 스택에 새로운 데이터를 삽입하는 행위
pop : 스택의 가장 마지막(최신) 데이터를 꺼내는 행위
top : 스택에서 가장 최신 데이터

## 언제 사용할까?
이전의 작업으로 되돌아갈 때 사용한다.
예) 구글 => 네이버 => 유튜브에서 `뒤로가기` 누르면 이전 웹사이트로 이동하거나, 문서작업시 Ctrl + z로 뒤로가기를 하듯이, 리스트에서 pop을 해서 이전의 데이터를 불러온다.

## 스택이 많이 쓰이는 알고리즘 유형
- 괄호 매칭
- 함수 호출(재귀 호출)
- 백트래킹
- DFS(깊이 우선 탐)

## 스택에서는 append와 pop을 이용하면 된다.
```python
lst = []

for i in range(int(input())):
    say = int(input())
    
    if say == 0:
        lst.pop()
        
    else:
        lst.append(say)
        
 
print(sum(lst))
```

# 2. 큐(Queue)
가장 오래된 데이터가 먼저 나간다. FIFO(First-in First- out, 선입 선출)
ex) 줄 설때도 가장 오래 기다린 사람이 카페 주문을 함으로 줄에서 벗어날 수 있는 것과 마찬가지.
가장 오래 기다린 데이터를 꺼내는 것 : Dequeue = pop(0)
맨 뒷 줄에 새로운 사람을 넣는 것 : Enqueue = append

## 언제 큐를 사용할까?
대기열 필요할때
- BTS 티켓팅 할 때
- 프로세스 관리(데이터 버퍼)
- 클라이언트/서버(Message Queue)