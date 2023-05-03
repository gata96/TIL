
# 1.홀수
list_odd = []
for i in range(7):
    nums = int(input())
    if nums %2 == 1:
        list_odd.append(nums)
        
if len(list_odd)==0:
    print(-1)


else:
    print(sum(list_odd))
    print(min(list_odd))
    
    
#2 더하기
saying = list(map(int, input().split(',')))        
print(sum(saying))

#3 학점계산


dic = {
'A+': '4.3', 'A0': '4.0', 'A-': '3.7',

'B+': '3.3', 'B0': '3.0', 'B-': '2.7',

'C+': '2.3', 'C0': '2.0', 'C-': '1.7',

'D+': '1.3', 'D0': '1.0', 'D-': '0.7',

'F': '0.0'
}
score = input()
print(dic[score])  # == print(dic.get(score))


po = list(input())

di = {'A':4, 'B':3, 'C':2, 'D':1, '+':+0.3, '0':+0.0, '-':-0.3}
if po == ['F']: print(0.0)
else:print(di[po[0]]+di[po[1]])


#4. 다이얼
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
second = 0
saying = input()

for i in range(len(saying)):
    #saying의 각 알파벳이 alphabt내에서 몇번째 인덱스에 속하는지?
    for alpha in alphabet:
        if saying[i] in alpha:
            second += alphabet.index(alpha) +3

print(second)

#5. 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
total = list(str(A*B*C)) # str으로 바꾼이유 : count가 문자밖에 인식을 못하기 때문

for i in range(10):
    print(total.count(str(i)))


#6. 회사에 있는 사람
dic = {}
num = int(input()) #출입기록 수 
for i in range(num):
    key, value = input().split()
    dic[key] = value # 딕셔너리에 넣기

for key, value in dic:
    if dic[key] == 'enter':
        print(key)





