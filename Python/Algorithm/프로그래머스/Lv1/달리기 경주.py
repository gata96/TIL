'''
문제 설명
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때,
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다.
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.
선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때,
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

'''

# 첫번째 아이디어: 이름이 불리면 인덱스가 한칸씩 줄어들어 앞으로 이동한다.

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
result = ["mumu", "kai", "mine", "soe", "poe"]

def solution(players,callings):
    for i in callings:
        idx = players.index(i)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players


# 문제 발생
# callings에서 나오는 이름을 players에서 매번 전 탐색하는 것은 시간이 많이 걸림
# 즉, callings 배열(크기:M)과 players 배열(크기:N)의 크기에 비례하기 때문에 시간복잡도는 둘의 곱인 O(MN)이 되어 이 방법으로 풀 수 없음
# 일반적으로 O(n)에서 n의 값이 1억을 넘으면 통과가 어렵다고 보면 되는데, 문제 조건을 보면 백만*5만=5백억이라는 수가 나

# 2번째 아이디어 : 딕셔너리 이용하기
# 딕셔너리 두 개 or 딕셔너리 하나와 리스트 하나가 필요

def solution(players,callings):
    # name:idx (선수이름:등수) 딕셔너리 만들기
    dic = {name:idx for idx, name in enumerate(players)} # 이름 = key, 인덱스 = value인 dictionary 만듦
    
    for name in callings: 
        # 지금 부른 선수의 인덱스를 찾는다.
        idx = dic[name]
        
        # idx를 가진 선수가 idx-1 선수를 추월한다.
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        # dic에 업데이트하기
        dic[players[idx]] = idx
        dic[players[idx-1]] = idx-1
        
    return players
    
    