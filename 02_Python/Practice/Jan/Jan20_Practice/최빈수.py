from statistics import multimode
T = int(input())

for t in range(1,T+1):
  num = int(input())
  
  for n in range(1, num+1):
    score = list(map(int,input().split()))
    print(f'#{num} {max(multimode(score))}')
