# 문제 1
number1 = 1
number2 = number1 + 1
print(number1,number2) # 1 2
#=============================================

# 문제 2
number1 = 10
number2 = 5
number3 = str(number1) +str(number2) # 숫자105가 아닌, 10과5의 문자 나열
number4 = number1 + number2
print(number1,number2,number3,number4) #105 15
#=============================================

#문제 3
string1= "Hello"
string2= string1
string3= "World" + "!"
print (string2, "?", string3) # Hello ? World!
#=============================================

#문제 4
string = "Hello?"
n=5
print(string*n) #Hello?Hello?Hello?Hello?Hello?
#=============================================

#문제 5 
string = "abc hello def"
sub_string1 = string[4:10] #4이상 10 미만, 공백도 문자열
sub_string2 = string[1:4]
sub_string3 = string[-1]
print(sub_string1) #hello 
print(sub_string2) #bc 
print(sub_string3) #f
#=============================================

#문제 6
number1 = 5
number2 = 10.0 +number1
number1 - 5 #변수 값에 할당된것이 없다.
number3 = number1 * (number2 + 10)
print(number1, number2, number3) #0 15.0 125
#=============================================

#문제 7
list_variable = [1,2,3,[1,2,3]]
sub_list = list_variable[3][-1]
print(sub_list) #3
#=============================================

#문제 8
list_variable =[]
list_variable.append(1)
print(list_variable)
list_variable.append("a")
print(list_variable)

list_variable[0] = 0
print(list_variable) #[0, 'a']
#=============================================

#문제 9
name = input("너의 이름은?")
print(name) #너의 이름은?
#=============================================

#문제 10
age = int(input("너의 나이는?"))
print("올해 나이 : ", age) # 올해 나이 :  25
print("내년 나이 : ", age+1) # 내년 나이 :  26