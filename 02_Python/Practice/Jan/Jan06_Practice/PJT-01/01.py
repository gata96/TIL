# 1. 텍스트 파일 데이터입력
# 아래의 내용을 01.txt에 기록하세요.

file = open('01.txt', 'w', encoding='UTF8')

print(file)

file.write ('Hello, Python!\n')

for n in range(1, 6):
    file.write (f'{n}일차 파이썬 공부 중\n')














file.close()