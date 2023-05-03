food = [1,7,1,2]

answer = ''
def solution(food):
    global answer
    for i in range(1,len(food)):
        mok = (food[i] // 2)  # mok = 3, 0, 1
        answer += str(i) * mok # 1113
    return print(answer+'0'+answer[::-1])

solution(food)
