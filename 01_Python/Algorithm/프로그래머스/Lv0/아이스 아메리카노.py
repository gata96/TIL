#방1
def solution(money):
    cup = money // 5500
    charge = money - cup * 5500
    result = []
    result.append(cup)
    result.append(charge)
    return result

# 방2
def solution(money):
    return [money//5500,money%5500]

# 방3
def solution(money):
    result = [money//5500,money%5500]
    return result