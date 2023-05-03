# 4. 텍스트 파일 데이터 활용 - 단어 등장 횟수
# 과일 데이터 fruits.txt를 활용하여 각 과일의 이름과 등장 횟수를 04.txt 에 기록하세요.
# 과일은 한 줄 당 1개만 기록되어 있습니다.


# 04.txt 생성 및 오픈
file = open('C:/Users/skswo/OneDrive/바탕 화면/TIL/Project/04.txt', 'w', encoding='utf-8' )


# fruits 파일 열고 읽기 (이미 'file'이라는 변수를 주었으므로 새로운 변수인 'f'로 설정)
with open('C:/Users/skswo/OneDrive/바탕 화면/TIL/Project/PJT-01/data/fruits.txt') as f:
    data = f.read()

# 엔터 단위로 리스트에 넣기
data_split = data.split()  # print(type(data_split)) #list

for word in data_split:   # 리스트 내 모든 요소 훑어보기
    cnt = data_split.count(word)   # 중복 요소 횟수 세기 & 횟수는 변수 cnt에 담기
    print(word, cnt)    # 요소와 횟수 프린트하기
    cnt_str = str(cnt)
                        # write('문자') 형태이기 때문에, str을 써서 cnt를 문자형으로 바꿔준다.
    file.write(word)    # 04.txt파일에 과일 적기
    file.write(' ')     # 과일 쓰고, 띄어쓰기
    file.write(cnt_str) # 횟수 적기
    file.write('\n')    # 엔터















