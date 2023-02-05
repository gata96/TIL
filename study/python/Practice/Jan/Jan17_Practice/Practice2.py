# # 1
T = int(input())


for t in range(1,T+1):
  count = int(input())
  numbers = list(map(int, input().split()))
  # print(numbers)
  print(sum(numbers))


  
# # 2

numbers = list(map(str, input().split()))
print(int(numbers[0]+numbers[1])+int(numbers[2]+numbers[3]))

# # 3
x_list = [] 
y_list = []

for _ in range(3):
  x,y = map(int, input().split()) #원소 받기
  y_list.append(y)

for i in range(3):
  if x_list.count(x_list[i]) == 1:
    x4 = x_list[i]
  if y_list.count(y_list[i]) == 1:
    y4 = y_list[i]

print(x4,y4)
  

# # 4

while True:
  a,b = map(int, input().split())

  if a == 0 and b == 0:
    break

  else:
    print(a+b)

# # 5

num = int(input())
list_num = []

for i in num:
  list_num.append(i)
  sum_num=sum(list_num)
  list_num.append(sum_num)
  print(list_num)

sum(map(int, str(num))) # map 함수를 활용하여 원소값 더하기
num = int(num)
