# 3. 텍스트 파일 데이터 활용 - 특정 단어 추출
# 과일 데이터 fruits.txt를 활용하여 이름이 berry로 끝나는 과일의 개수와 목록을 03.txt 에 기록하세요.

# 과일은 한 줄 당 1개만 기록되어 있습니다.


with open ('C:/Users/skswo/OneDrive/바탕 화면/TIL/Project/PJT-01/data/fruits.txt') as f:
    data = f.read()

# print(type(data)) #str


### 파일 읽기
# with open(경로) as f:
#     변수 = f.read()


# berry로 끝나는 과일찾기
box = []
for word in data:
    if 'berry' in data:
        box.append(word)
        print(word)


# 개수
# 목록

# 03에 만들고, 적기

