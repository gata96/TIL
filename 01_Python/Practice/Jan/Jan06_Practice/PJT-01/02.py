# 2. 텍스트 파일 데이터 입출력
# 과일 데이터 fruits.txt를 활용하여 작성된 총 과일 개수를 02.txt 에 기록하세요.

# 과일은 한 줄 당 1개만 기록되어 있습니다.


with open('C:/Users/skswo/OneDrive/바탕 화면/TIL/Project/PJT-01/data/fruits.txt',encoding = 'utf-8') as f:
    data = f.read()

data1 = data.split('\n')
# print(data1) #list
print(len(data1)) #394
print(str(len(data1)))


file = open('C:/Users/skswo/OneDrive/바탕 화면/TIL/Project/02.txt', 'w',encoding = 'utf-8' )
file.write(str(len(data1)))









