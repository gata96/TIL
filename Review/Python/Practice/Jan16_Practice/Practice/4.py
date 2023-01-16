# 첫 번째 줄에 설문조사를 한 사람의 수 N (1 ≤ N ≤ 101, N은 홀수)가 주어진다.
# 다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다. 0은 준희가 귀엽지 않다고 했다는 뜻이고, 1은 준희가 귀엽다고 했다는 뜻이다.
# 준희가 귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고 귀엽다는 의견이 많을 경우 "Junhee is cute!"를 출력하라.


# list = []

# for n in range(int(input())): # 사람 수만 큼 for 문
#     num = int(input()) # 0이나 1입력 받기
#     list.append(num) # 입력 받은 거 리스트로 넣기

#     opinion += int(input())

# count1 = list.count(1) # 리스트 내에서 1의 개수
# count0 = list.count(0) # 리스트 내에서 0의 개수

# if count1 > count0:
#     print('Junhee is cute!') # 만약 1 개수가 많으면 '준희는 귀엽다'

# else:
#     print('Junhee is not cute!') # 만약 0 개수가 많으면 '준희는 안 귀엽다'



# 스터디 내 다른 풀이 방법


N = int(input())
opinion = 0

for n in range(N):
    opinion += int(input())

if opinion > N/2:
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')







