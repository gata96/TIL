X = "100"
Y = "123450"
answer = []
for i in set(X)&set(Y):# 교집합
    answer.append(i)
    answer = sorted(answer, reverse=True)
if len(answer) == 0:
    print('-1') 
if answer[0] == '0':
    print('0')
    
print(''.join(answer))
