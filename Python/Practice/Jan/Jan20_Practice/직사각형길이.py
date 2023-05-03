A = list(map(int, input().split()))

for i in range(3):
    
    if A.count(A[i]) == 1:
        print(A[i])

    elif A.count(A[i]) == 3:
        print(A[0])
        

    
    
        
        



