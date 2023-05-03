#최소, 최대

N = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))


# 숫자의 합
N = int(input())
num = list(map(int, input()))
print(sum(num))

# 수 정렬하기
N = int(input())
list_num =[]

for i in range(N):
    num = int(input())
    list_num.append(num)
    
    new = sorted(list_num)

print(*new,sep = '\n')

'''
# a1 = [1,9,4]
# a2 = a1.sort()
# print(a1) # [1, 4, 9]  원본값이 정렬됨
# print(a2) # None a1의 리턴값이 None이다.


# b1 = [1,9,4]
# b2 = sorted(b1)
# print(b1) #[1, 9, 4]    원본값이 바뀌지 않음
# print(b2) #[1, 4, 9]    정렬된 새 리스트 생성됨
'''

# 최댓값
num_list= []
for i in range(9):
    num = int(input())
    num_list.append(num)
a = max(num_list)
print(a)
print(num_list.index(a)+1)






