k = 3
score = [10, 100, 20, 150, 1, 100, 200]



def solution(k,score):
    lst = [] # 명예의 전당
    answer = [] # 발표 점수
    for i in range(len(score)):
        lst.append(score[i])
        if len(lst) <= k and score[i] < min(lst): # 1~3일차 (예 5일차)
            continue
            
        elif len(lst) > k: # 4일차
            lst = sorted(lst)
            lst.pop(0)
        answer.append(min(lst))
    return print(answer)
        
solution(k,score)
        