# 옹알이1
def solution(babbling):
    answer = 0
    for i in babbling:
        while i:
            if i[:3] in ["aya", "woo"]:
                i = i[3:]
            elif i[:2] in ["ye", "ma"]:
                i = i[2:]
            else:
                break
        if i == "":
            answer += 1
    return answer

babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))

# 다음에 올 숫자
def solution(common):
    if common[1] - common [0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    
    elif common[1] // common[0] == common[2] // common[1]:
        return common[-1] * (common[1] // common[0])


# 연속된 수의 합
def solution(num,total):
    mid = total // num
    half = num // 2
    top = mid + half + 1
    bottom = top - num
    
    answer = [i for i in range(bottom, top)]
    return answer

# 종이 자르기


def solution(M, N):
    return (M*N)-1