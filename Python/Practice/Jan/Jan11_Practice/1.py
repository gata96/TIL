f = open('input.txt', 'w')
print(f)
f.write

# #문제1

numbers = list(map(int, input().split()))
# print(*numbers)
# print(' '.join(numbers)) #TypeError: sequence item 0: expected str instance, int found
# join 할때는 string 필요
print(*numbers)


# 문제 2
# 공백으로 구분된 문자열

# Lorem ipsum dolor sit amet, consectetur adipiscing elit.

string = input().split()
print(string)
print(*string) 
# 또는
print(' '.join(string))


# 문제 3
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스 수가 주어집니다.

# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.

T = int(input())


for t in range(1, T+1):
    
    N = int(input())
    for n in range(1,N+1):
        print(n)



# 문제 4
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스 수가 주어집니다.

# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    for n in range(N+1):
        print(n, n)


# 문제 5
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스 수가 주어집니다.

# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.

# 각 문장에 포함된 단어를 공백을 기준으로 출력하세요.

T = int(input())

for t in range(1, T+1):
    N = int(input())
    for n in range(1, N+1):
        string = input().split()
        print(*string)

# 문제 6
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스 수가 주어집니다.

# 각 테스트 케이스의 첫 번째 줄에 입력 줄 수가 주어집니다.

T = int(input())

for t in range(1, T+1):
    N = int(input())

    for n in range(N):
        numbers = list(map(int, input().split()))
        print(*numbers)

# 문제 7
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.

T, N = list(map(int, input().split()))

for t in range(1, T+1):
    N = int(input())

    for n in range(1, N+1):
        pass


# 문제 8
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.


T, N = list(map(int, input().split()))

for t in range(1, T+1):
    for n in range(1, N+1):
        numbers = list(map(int, input().split()))


# 문제 8
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.

# 문제 9
# 테스트 케이스 수와 입력 줄 수가 주어지는 입력

# 첫 줄에 테스트 케이스와 각 테스트 케이스의 입력 줄 수가 주어집니다.

T, N = list(map(int, input().split()))

for t in range(1, T+1):
    for n in range(1, N+1):
        numbers = list(map(int, input().split()))
        