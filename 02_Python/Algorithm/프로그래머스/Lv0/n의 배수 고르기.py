# 파이썬 [프로그래머스_Lv.0_n의 배수 고르기]
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

n = 12
numlist= [2, 100, 120, 600, 12, 12]

# 방1
def solution(n):
    result = []
    for i in numlist:
        if i % n == 0:
            result.append(i)
    return result
print(solution(n))

# 방2
def solution(n, numlist):
    return [i for i in numlist if i % n == 0]
print(solution(n, numlist))

# 방3
def solution(n, numlist):
    return list(filter(lambda v: v % n == 0, numlist))
