# 문제 1
# number = int(input('숫자를 입력해주세요 > '))
# print(number +10)

# 문제 2 
# food = str(input('좋아하는 음식을 입력해주세요 >')) 
# print('좋아하는 음식 : ', food)

## str 있고 없고 여부는 상관없다. int가 애초에 문제열을 입력받는 함수이기 때문이다.
## 즉, food = str(input('...)) 와 food = intput('...') 는 같다.

# 문제 3
# 방법1
# name = input('이름을 입력해주세요 > ')
# age = int(input('태어난 년도를 입력해주세요 > '))
# print('저의 이름은',name+'이고, 올해 나이는', str(2024-age)+'세 입니다.')
## '+'는 공백 없이 이어붙여주고 ','는 공백있게 이어 붙여준다.
## '+'는 문자(str)에서만 쓸 수 있다. int는 str로 바꿔줄 것!

# 방법2 (완전 꿀팁)
# name = input('이름을 입력해주세요 > ')
# age = int(input('태어난 년도를 입력해주세요 > '))
# a = 2024 - age
# print(f'저의 이름은 {name}이고, 올해 나이는 {a}세 입니다.')


# 문제 4
# first_line = input('첫 번째 문장을 입력해주세요 > ')
# second_line = input('두 번째 문장을 입력해주세요 > ')
# print(first_line+second_line)

# 문제 5
# number = int(input('숫자를 입력해주세요 > '))
# print('-'+number)

# 문제 6
# first_number = int(input('첫 번째 숫자를 입력해주세요 > '))
# second_number = int(input('두 번째 숫자를 입력해주세요 > '))
# print('더하기 연산 :', first_number+second_number)
# print('빼기 연산 :', first_number-second_number)
# print('곱하기 연산 :', first_number*second_number)
# print('몫 연산 :',first_number//second_number)
# print('나머지 연산 :',first_number%second_number)

# 문제 7
# first_number = int(input('첫 번째 숫자를 입력해주세요 > '))
# second_number = int(input('두 번째 숫자를 입력해주세요 > '))
# third_number = int(input('세 번째 숫자를 입력해주세요 > '))
# print(int((first_number+second_number+third_number)/3))

# 문제 8
# first_number = int(input('첫 번째 숫자를 입력해주세요 > '))
# second_number = int(input('두 번째 숫자를 입력해주세요 > '))
# third_number = int(input('세 번째 숫자를 입력해주세요 > '))
# fourth_number = int(input('네 번째 숫자를 입력해주세요 > '))
# fifth_number = int(input('다섯 번째 숫자를 입력해주세요 > '))
# list =[first_number,second_number,third_number,fourth_number,fifth_number]
# print(list)

# 문제 9
# letter = input('문자열을 입력해주세요 > ')
# number = int(input('숫자를 입력해주세요 > '))
# print(letter*number)

# 문제 10
# first_number = int(input('첫 번째 숫자를 입력해주세요 > '))
# print(first_number)
# second_number = int(input('두 번째 숫자를 입력해주세요 > '))
# print(first_number+second_number)
# third_number = int(input('세 번째 숫자를 입력해주세요 > '))
# print(first_number+second_number+third_number)
# fourth_number = int(input('네 번째 숫자를 입력해주세요 > '))
# print(first_number+second_number+third_number+fourth_number)
# fifth_number = int(input('다섯 번째 숫자를 입력해주세요 > '))
# print(first_number+second_number+third_number+fourth_number+fifth_number)
