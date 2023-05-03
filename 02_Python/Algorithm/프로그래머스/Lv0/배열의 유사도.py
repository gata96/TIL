# 파이썬 [프로그래머스_Lv.0_배열의 유사도]
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

# case 1
s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

# case 2
s1 = ["n", "omg"]
s2 = ["m", "dot"]

def solution(s1,s2):
    result = 0
    for i in s1:
        if i in s2:
                result += 1
    return result
   
print(solution(s1,s2))