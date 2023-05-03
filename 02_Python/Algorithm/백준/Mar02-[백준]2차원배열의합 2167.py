n,m = map(int,input().split())
s = []
r = [[0]*(m+1) for _ in range(n+1)]

# 리스트 s = n* m의 2차원 배열
for _ in range(n):
    s.append(list(map(int,input().split())))

# 리스트 r : 1행 1열이 0인 n+1, m+1의 2차원 배열
for i in range(1,n+1):
    for j in range(1,m+1):
        r[i][j] = s[i-1][j-1] + r[i-1][j] + r[i][j-1] - r[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(r[x][y]-r[x][j-1]-r[i-1][y]+r[i-1][j-1])