t = "3141592"
p = "271"
# result = 2

# 방1
def solution(t,p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return print(answer)

solution(t,p)

# 방2
def solution(t,p):
    return print(sum(int(t[i:i+len(p)]) <= int(p) for i in range(len(t)-len(p)+1)))

solution(t,p)
