# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값

n = int(input())

# 방1
cnt = 0
for _ in range(2,n+1):
    if _ % 2 == 0:
        cnt += _
print(cnt)
    
# 방 2
print(sum([_ for _ in range(2, n+1,2)]))