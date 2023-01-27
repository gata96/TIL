# # # 세 수
# # lst = list(map(int, input().split()))
# # lst_s= sorted(lst)
# # print(lst_s[1])

# # # 고무오리 디버깅
import sys
lst = []
input = sys.stdin.readline
while True:
    my = input().rstrip()
    

    if my == '고무오리 디버깅 끝':
        break
    if my == '고무오리 디버깅 시작':
        continue    
    if my == '문제':
        lst.append(my)
    elif my == '고무오리':
        if len(lst) == 0:
            lst.append('문제')
            lst.append('문제')
        else:
            lst.pop()
    
if len(lst) != 0:
    print('힝구')
else:
    print('고무오리야 사랑해')




# # # 대칭 차집합
# a, b = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# total = A+B
# result = 2*len(set(total))-len(total)
# print(result)

# # # 나머지
# lst = []
# for i in range(10):
#     num = int(input())
#     lst.append(num % 42)
# print(len(set(lst)))

# # # 단어정렬
# import sys
# input = sys.stdin.readline
# lst = []
# cnt = int(input())

# for i in range(cnt):
#     lst.append(input().strip())
#     result = sorted(list(set(lst)), key = len)

# print(result)




