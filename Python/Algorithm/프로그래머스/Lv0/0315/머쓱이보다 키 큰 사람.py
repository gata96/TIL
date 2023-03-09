# 방1
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# 방2
def solution(array, height):
    array.append(height)
    array_s = sorted(array, reverse = True) # 내림차순
    return array_s.index(height) # 인덱스 구하기
