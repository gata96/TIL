# 파이썬 [프로그래머스_Lv.0_자릿수 더하기]
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.

n = 1234

# 방1
def solution(n): # n = 1234
    strN= str(n) # n을 문자열로 바꾸기
    answer = 0
    for i in range(len(strN)):
        answer += int(strN[i]) 
        # 문자열도 리스트처럼 인덱스 사용 가능
        # 인덱스 값이 문자니까 정수로 변환
    return answer
print(solution(n))

# 방2
def solution(n):
    N=[int(i) for i in str(n)]
    return sum(N)
print(solution(n))
