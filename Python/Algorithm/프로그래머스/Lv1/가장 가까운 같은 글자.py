s = "foobar"

result = [-1] # 첫번째는 항상 -1

for i in range(len(s)):
    if s[i+1] != s[i]:
        result.append(-1)
    else:
        idx = int(s[i+1].index) - int(s[i].index)
        result.append(idx)
print(result)
    