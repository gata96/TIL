# 문제 1 🎈
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# 단, index() / find() 메서드는 사용하지마세요.

# string = input('문자열을 입력하세요 > ')
# total=[]

# for str in string:
#     if str == 'e':
#         total += str
#         print(total)



# e발견
# 몇 번째? 
# e까지 리스트에 담아
# 리스트안의 원소 개수 세고 -1


# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# string = input('문자열을 입력하세요 > ').split()

# dic = {}

# for str in string:
#     if str in dic:
#         dic[str] += 1
    
#     else:
#         dic[str] = 1

# print(dic)

# 만약 split()이 없으면, 문자열을 입력하세요 > hello word
# {'h': 1, 'e': 1, 'l': 2, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1} 이렇게 나온다.

# 문제 3. 문자열을 입력받고, e 를 제거한 결과를 출력하세요. 
# 단, replace() 메서드는 사용하지 마세요.

# string = list(input ('문자열을 입력하세요 > '))

# for str in string:
#     if 'e' in string:
#         string.remove('e')
#          # remove는 리스트의 요소를 삭제하는 것이기 때문에, str가 아닌, string을 사용해야한다.

# result =''.join(string) # 리스트를 문자열로 합치기 

# 문제 4 🎈
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 문제 5
# 단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.

# 단, join() 메서드는 사용하지마세요.

# string = input('문자열을 입력하세요 > ')

# result = string.replace(' ','-')

# print(result)

# 문제 6 🎈
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.

# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

# number = int(input('양의 정수를 입력하세요'))
# list_number = list(number)
# print(list_number)
# for i in list_number:
#     list_number.append(i)

# print(list_number)


number = range(int(input()))

print(type(number))
print(number)