import sys
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

T = int(input())
lst = ['a','e','i','o','u']

for t in range(1, T+1):
    string = input()
    for i in lst:
        if string.find(i):
            string.remove(i)
    print(string)

