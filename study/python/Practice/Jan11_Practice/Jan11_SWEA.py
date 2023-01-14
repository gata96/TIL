# 문제 1. 소문자를 대문자로 바꾸기

print(input().upper())


# 문제 2. 주어진 모든 수 더하기

number = int(input())
total = 0
for i in range(1,number+1):
    total += i
print(total)

n = int(input())
a = range(1, n+1)
print(sum(a))





# 문제 3. 1대1 가위바위보

a, b = list(map(int, input().split()))

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
    
if a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')

if a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')


# 4. 자릿수 더하기

# 숫자를 문자로 바꾼다
# 문자길이 만큼 각 자릿값을 가져온다.
# 각 자리 값을 숫자로 변환해 변수에 합한다.

N = int(input())
total = 0
for n in str(N):
    total += int(n)

print(total)

# 5. 더블더블

cnt = int(input())

for number in range(cnt+1):
    
    result = 2** number
    print(result, end = ' ')

# 6번. 대각선 출력하기

for i in range(0,5):
    for j in range(0,5):
        if i == j:
            print('#',end ='')
        
        else:
            print('+',end ='')
    
    print()

