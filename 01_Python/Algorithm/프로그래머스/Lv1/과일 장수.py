k = 4 # 사과 최대 점수
m = 3 # 한 상자에 담을 사과 수
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2] # 사과 점수
result = 33 # 최대 이익



def solution(k,m,score):
    answer = 0
    score = sorted(score,reverse=True) # [4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 1, 1]
    for i in range(len(score) // m): # 3개씩 잘라서 4묶음
        answer += score * m
        return print(answer)
    
solution(k,m,score)
    
    