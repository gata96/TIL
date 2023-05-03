
def solution(babbling):
    answer = 0
    prono = ['aya','ye','woo','ma']
    for i in babbling :
        for j in prono :
            if j+j in i :
                break
            else :
                i = i.replace(j,"").strip()
        if i :
            continue
        else :
            answer += 1
        
    print(answer)

def solution(babbling):
    count = 0
    baby = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in baby:
            if j+j in i:
        
        if      
#         if i in babbling:
#             count += 1
#         elif 
#     return count

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