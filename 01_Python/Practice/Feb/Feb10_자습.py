import sys
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

T = int(input())

for t in range(1,1+T):
    num = int(input())
    A = list(map(int,input().split()))
    print(f'#{t} {max(A)-min(A)}')
    

