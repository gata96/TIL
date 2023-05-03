# SWEA 1933
# a =int(input())

# for i in range(1, a+1):
#     if a % i == 0:
#         print(i, end=' ')

# 백준 음계
# N = list(map(int,input().split()))
# # print(N[::-1])
# if N == sorted(N):
#     print('ascending')
# elif N == sorted(N, reverse = True):
#     print('descending')
# else:
#     print('mixed')

lst = ['C','A','M','B','R','I','D','G','E']
says = input()
for i in says:
    if i in lst:
        says.delete(i)
    print(says)