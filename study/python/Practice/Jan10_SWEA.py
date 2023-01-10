# 문제 1
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.


# 두 수를 입력받기

T = int(input('test case'))


for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    
    몫 = a // b
    나머지 = a % b
    
    print(f'#{t} {몫} {나머지}')

#=========================================================
# 문제2
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
T = int(input())


for t in range(1,T+1):
    numbers = list(map(int, input().split()))
    average = round(sum(numbers)/len(numbers))

    print(f'#{t} {average}')

#=========================================================

# 문제3
# 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.
# [제약 사항]

# 1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)

# 2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.

# 3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.

a, b = list(map(int, input().split()))

# 두개의 자연수 입력 받기
# 사칙연산 출력하기

A = a + b
B = a - b
C = a * b
D = a / b

# 소수점이하의 숫자 버리기(math모듈사용)
import math

print(math.floor(A)) # 소수점 이하 버림
print(math.floor(B))
print(math.floor(C))
print(math.floor(D))
# ##for문으로 작성할 수는 없었을까?
#=========================================================

# 문제4

# 주어진 숫자만큼 # 을 출력해보세요.
# 주어질 숫자는 100,000 이하다.

number = int(input())

for i in range(1,number+1):
    '#'
print('#'*i)
#=========================================================

# 문제5

T = int(input('test case'))


for t in range(1,T+1):
    numbers = list(map(int, input().split()))
    print(f'#{t} {max(numbers)}')
    


    
