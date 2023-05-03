# 문제설명 : ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16=(5 + 10 + 1)점이 됩니다.
# photo는 이중 리스트. photo의 각각의 원소 = 하나의 리스트

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# result = [19,15,6]

def solution(name,yearning,photo):
    result = []
    score = 0
    dic = {n:y for n,y in zip(name,yearning)}
    # zip : 튜플 형태로 name과 yearning의 각 원소를 차례로 묶음
    
    # print(n,y)
    # (may, 5)
    # (kein, 10)
    
    # photo 탐색
    for pho in photo: # 2중 리스트니까 2중 for문으로! 
        for p in pho:
            if p in dic.keys(): # 그 원소가 dic의 key값으로 존재하는가?
                score += dic[p] # key값의 value를 score에 담기
        result.append(score) # score값을 result 리스트에 차례로 담아주기
    
    return result