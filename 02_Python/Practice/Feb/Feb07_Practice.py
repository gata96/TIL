# # ## 막대기 -> 시간초과
# import sys
# sys.stdin = open('input.txt','rt')
# input = sys.stdin.readline

# 6 9 7 8 6 4 6
lst = [int(input()) for i in range(int(input()))]
cnt = 1

for l in lst[::-1]:
    if l > lst[::-1][0]:
        cnt += 1
print(cnt)

# # ## 덩치 

T = int(input())
lst = []
for t in range(T):
    a, b = list(map(int,input().split())) # 키랑 몸무게 input 받기
    lst.append((a, b)) # 리스트에 저장
    
# print(lst) 
# [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

for i in lst: # 키를 i, 몸무게를 j로 각각 서로 비교해야하기 때문에 이중 for문 사용
    rank = 1
    for j in lst:
        if i[0] != j[0] and i[1] != j[1]: # 키와 몸무게가 둘다 서로 다른 경우
            if i[0] < j[0] and i[1] < j[1]: # 키가 더 크고, 몸무게가 더 큰 경우
                rank += 1 # rank = 2 
    print(rank) # 제일 키와 몸무게가 큰 경우, 다들 자기보다 작으니까 rank값이 안올라감.
    
# # ## 킹 
# # # 델타값을 이용한 탐색과 아스키 코드 사용
# # # 딕셔너리 사용 : 방향이 알파벳임으로 알파벳을 키로 잡는다.

directions = {
    'R': (0,1),
    'L': (0,-1),
    'B': (1,0),
    'T': (-1,0),
    'RT': (-1,1),
    'LT': (-1,-1),
    'RB': (1,1),
    'LB': (1,-1)
}

# 체스판의 알파벳->숫자좌표로 변환하기 위해서 아스키코드 사용
k, s ,n = input().split() # 킹 위치, 돌 위치, 움직이는 횟수

kx, ky = 8 - int(k[1]), ord(k[0])-ord('A') # kx, ky : king이 x,y 축으로 얼만큼 이동하는지
sx, sy = 8 - int(s[1]), ord(s[0])-ord('A') # sx, sy : stone이 x,y 축으로 얼만큼 이동하는지
# print(kx,ky) # 7 0
# print(sx,sy) # 6 0

for _ in range(int(n)): # 리스트를 딕셔너리의 키로 사용하려면 에러가 남.
    

    dx, dy = directions[input()] # 이동할 거리
    
    if not (0 <= kx+dx < 8 and 0 <= ky+dy < 8): # king과 stone 모두 격자를 나가면 무효처리
        continue
    kx += dx # king의 현재 위치
    ky += dy 
    
    # king과 stone이 나란히 이동할 때
    if (kx, ky) == (sx,sy): # king은 stone 위치로 이동
        if not (0 <= sx+dx < 8 and 0 <= sy+dy < 8): # stone이 격자 밖으로 밀리는 경우 다시 되돌리기
            kx -= dx
            ky -= dy
            continue
        # stone은 앞으로 전진
        sx += dx
        sy += dy
# 모두 이동한 후 숫자를 문자로 바꿔줘야한다. chr 사용
print(chr(ord("A")+kx)+str(8-ky)) 
print(chr(ord("A")+sx)+str(8-sy))
         