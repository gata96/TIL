number = 10
limit = 3
power = 2
# result = 21

# 10의 약수 = 1,2,5,10 10의 제곱근 = 3.xx => int => 3
# 9의 약수 = 1,3,9

# 약수의 개수 구하는 함수 만들기
def get_cds(number, limit , power):
    cnt = 0
    for i in range(1,int(number**(1/2))+1):
        if number % i == 0:
            if i == number**(1/2): # 9의 약수
                cnt += 1
            else: # 10의 약수
                cnt += 2
        if cnt > limit:
            return power
    return cnt

# 약수 합하기
def solution(number, limit , power):
    total = 0
    for i in range(1,number+1):
        count = get_cds(i, limit , power)
        total += count
        
    return print(total)
solution(number, limit , power)


    
