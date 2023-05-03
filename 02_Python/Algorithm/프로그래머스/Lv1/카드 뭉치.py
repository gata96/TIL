cards1 = ["i", "water", "drink"]	
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]


# card1과 card2가 goal의 순서 배열과 같은지 여부를 따진다.

def solution(cards1, cards2, goal):
    
    for g in goal:
        if cards1 and cards1[0] == g:
            del cards1[0]
        elif cards2 and cards2[0] == g:
            del cards2[0]
        else:
            return print("No")
    return print("Yes")


solution(cards1, cards2, goal)
