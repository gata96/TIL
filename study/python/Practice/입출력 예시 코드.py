# 정수 1개 입력 받기

number = int(input())


# 공백으로 구분된 여러개의 정수 입력 받기

numbers = list(map(int, input().split()))



# 공백으로 구분된 여러개의 단어 입력 받기

string = input().split()



# 공백으로 구분된 2개의 정수 입력 받기

a, b = list(map(int, input().split()))



# 테스트 케이스 수가 주어지는 입력 받기

T = int(input())

for t in range(1, T+1):
    print(t)
    # 입력코드
    pass




# 입력 줄 수가 주어지는 입력 받기

N = int(input())

for _ in range(N):
    #입력코드
    pass




# 테스트 케이스와 입력 줄 수가 주어지는 입력 받기

T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수

    for _ in range(N):
        #입력 코드
        pass


    

# 파일 입력

# input.txt 파일을 생성하고,입력을 작성해주세요.
# 코드를 알고리즘 사이트에 제출할 때 아래 두 줄은 주석처리 해주세요.
import sys
sys.stdin = open("input.txt", "r")

# 이하 입력 코드
