numbers = [1, 2, 3, 4, 5]

# 방1
answer = []
for num in numbers:
    answer.append(num*2)
print(answer)

# 방2.리스트 컴프리헨션
print([num*2 for num in numbers])

# 방3. 람다
print(list(map(lambda x: x * 2, numbers)))