lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 방법1
total = 0 
for _ in lst:
    total += _
print(total / len(lst))

# 방법2
print(sum(lst)/len(lst))
