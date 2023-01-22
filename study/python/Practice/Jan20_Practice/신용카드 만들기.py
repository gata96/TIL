import math
T = int(input())
odd = [0,2,4,6,8,10,12,14]
even = [1,3,5,7,9,11,13]
total1 = 0
total2 = 0
N = int()
for t in range(1,T+1):
    num = list(map(int, input().split()))

    for i in odd:
        total1 += num[i]*2

    for j in even:
        total2 += num[j]


    total = total1 + total2
    print(total)
    
'''
    if (total + N) % 10 == 0:
        print(N)
'''     








