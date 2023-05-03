T = int(input())

for t in range(1, T+1):

    A, B = list(map(int, input().split()))
    print(f'Case #{t}: {A+B}')