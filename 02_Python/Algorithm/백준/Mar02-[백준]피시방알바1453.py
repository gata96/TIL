n = int(input())
ppl = map(int, input().split())
print(n-len(set(ppl)))