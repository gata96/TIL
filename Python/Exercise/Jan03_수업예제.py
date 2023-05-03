
a = -10
if a> =10:
    print('양수')
else:
    print('음수')

print(a)

#==========================================================

num = int(input('숫자 입력하세요'))

if num % 2 == 0:
    print('짝수')

else:
    print('홀수')

#==========================================================

%-format
name = 'kim'
score = 4.5
print('hello, %s' %name)
print('내성적은 %d' %score)
print('내성적은 %f' %score)

#==========================================================

name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}' )
# Hello, Kim! 성적은 4.5

#==========================================================

pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*4}')

#==========================================================

print(True + 3) #4
print(5.0 + 3) #8.0
print(3+5+4j) #(8+4j)
print(float('3.5') +4)

#==========================================================

if <표현식>:
    <Run here>
else: 
    <or not, Run here>

#==========================================================

a = -10
if a >= 0:
    print('양수')  
else:
    print('음수')  
print(a)

#==========================================================

num = int(input('입력해주세요 > '))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

#==========================================================

dust = int (input('입력'))

if dust<= 30:
    print('좋음')

if 30< dust <= 80:
    print('보통')

if 80< dust <= 150:
    print('나쁨')

else:
    print('매우나쁨')

print('미세먼지 확인 완료')

#==========================================================

dust = int (input('입력'))
if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('실외활동을 자제하세요')
elif dust > 80:
    print('매우 나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('값이 잘못되었습니다')
    else:
        print('좋음')

print('미세먼지 확인 완료')

#==========================================================

print(type(range(4)))
print(list(range(3)))
print(list(range(1,5)))
print(list(range(1,5,2)))
print(list(range(6,1,1)))

#==========================================================

for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')

#==========================================================

chars = input()

for char in chars:
    print(char)

#==========================================================

chars = input() #gata
print(len(chars)) #4
print(range(len(chars))) #range(0,4)
print(range(4)) #range(0,4)
print(range(0,4))

#==========================================================

chars = input()
# range(chars) -> ❌ # range(문자) 불가능. len거쳐야한다.
# len(chars)
range(len(chars))
for idx in range(len(chars)): #idx:0,1,2,3
    print(chars[idx])

#==========================================================

for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
        break
    print(i)
    
#==========================================================

for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

#==========================================================

for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다')

#==========================================================

for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')