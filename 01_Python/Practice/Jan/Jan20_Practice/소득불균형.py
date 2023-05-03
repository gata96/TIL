T = int(input())


for t in range(1, T+1):
    under_cnt = 0
    sum = 0
    N = int(input())
    num = list(map(int, input().split()))

    for i in num:
        
        sum += i
        count = len(num)
        avg = sum/count
    
        for i in num:
            if i<= avg:
                under_cnt += 1 

    print(f'#{t} {under_cnt}')
    




