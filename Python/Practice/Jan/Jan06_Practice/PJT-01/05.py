# 아래 코드 수정 금지

import json

movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
# 5. JSON 데이터 활용 - 영화 단일 정보
# 영화 데이터 movie.json 을 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하세오.

# 코드 작성 전 movie.json 의 데이터 구조를 파악하세요.
# movie.json 파일에서 읽은 데이터는 변수 movie 에 저장됩니다.
# 아래 정보를 가진 딕셔너리를 출력하세요.
# id
# title
# vote_average
# overview
# genre_ids

print(type(movie_json))