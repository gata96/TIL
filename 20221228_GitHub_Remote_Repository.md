# 원격저장소 GitHub

- GitHub은 구글 드라이브 처럼 파일/폴더를 삭제,수정,변경,할 수 있는 서비스가 아니라, 최신 버전(커밋)을 관리하는 버전관리 시스템이다.

Q. 로컬드라이브에서 파일 삭제하면 GitHub에서 사라지나?
=> 삭제 후, add & commit까지 해야 GitHub에 반영된다.

## 학습목표
- `원격저장소` 활용 `명령어`를 이해하고 설명할 수 있다.
- `분산버전관리 시스템`을 이해하고 설명할 수 있다.
- GitHub 원격저장소에 로컬저장소를 올려 `관리`할 수 있다.

<br>

# 분산버전관리시스템 복습

- 중앙집중식 버전관리 시스템
    - `중앙 서버에서만 버전을 관리`하고 로컬에서는 파일을 편집

<br>

- 분산버전관리시스템
    - `로컬에서도 버전을 기록, 관리`하고 `원격 저장소(Remote repository, 즉, GitHub)`를 활용하여 협업한다.

<br>


# 원격저장소 GitHub 설정하기

    $ git push
    - 로컬 저장소(유저 컴퓨터)의 버전을 원격저장소(GitHub)로 보낸다.

    $ git pull
    - 원격저장소의 버전을 로컬 저장소(유저 컴퓨터)로 가져온다.

1) GitHub New Repository 만들기

2) 저장소 이름 설정 (예: test)

3) URL 확인 & 복사

`https://github.com/gata96/test.git`

    gata96 :깃헙 유저네임
    test: 저장소 이름

4) 로컬저장소에 원격 저장소 정보 입력하기
즉, 내 vs code에 github주소 가져오기

`$ git remote add origin https://github.com/gata96/test.git`

    *"git아, 원격저장소를 추가해. (원격저장소의 이름은) origin이야."*

5) 원격저장소 정보 확인

`$ git remote -v`

<br>

6) 로컬의 commit된 버전을 github에 Push하기

`$ git push origin master`

    $ git push <원격저장소이름><브랜치이름>



github는 로컬 폴더/파일을 삭제,수정,변경하는 등 관리하는 곳이 아니라, 커밋된 최신 버전만을 볼 수 있는 곳이다.

<br>

7) 로컬 저장소의 버전을 원격저장소로 Pull하기

`$ git pull origin master` 

    $ git pull <원격저장소><브랜치이름>



8) 원격저장소 삭제

`$ remote rm origin`

    $ remote rm <원격저장소>

<br>

# 프로젝트에 Join하고 싶을때, Clone 이용하기
- Github에 있는 `.git저장소까지 모든 버전`을 로컬로 가져오는 것.

    $ git clone <원격저장소 주소>


## 1) Clone과 Pull의 차이점?

- Pull은 GitHub에 올라온 **가장 최신 버전(커밋)**의 파일/폴더를 다운받는 것
- Clone은 **.git 저장소까지 모든 버전(옛날,최신 모두)**의 파일/폴더를 복제하여 가져오는 것.


## 2) Question

(1) 로컬에서 새로운 프로젝트를 시작하고 싶어요.
- .git저장소도 없는 상태
- `$ git init`으로 로컬에 `.git`저장소부터 만들기

<br>

(2) 다른 사람들이 하고 있는 원격에 존재하는 프로젝트에 Join하고 싶어요. 

(협업프로젝트, 외부 오픈소스 참여)
- clone(복제) 이용하기
-`$ git clone <원격저장소 주소>`

<br>

(3) 프로젝트 개발 중 다른 사람의 커밋을 받아오고 싶어요.
- 가장 최신 버전만을 가져오는 것이므로 pull이용하기
- `$ git pull origin master`

<br>

(4) 내가 한 로컬 프로젝트 개발을 깃헙에 공유하고 싶어요.
- 작성 -> add -> commit -> `github에 업로드`
- `$ git push origin master`

<br>


# Push Conflict (오류창)
![1](push_conflict.png)

- 로컬과 원격의 `커밋 내용이 달라서` 발생한 것임.
- 원격의 버전을 로컬로 `pull`하면, 로컬에서 두 커밋이 결합되고 `새로운 커밋`이 탄생한다.
- 이 New 커밋을 원격(GitHub)으로 `push`하면 해결됨.

<br>

# gitignore

- 굳이 GitHub에서 `관리할 필요 없는 (=버전관리랑 상관없는)` 파일/폴더들을  vs code에서 예외처리하는 것. ex) 엑셀파일

- vs code의 새로운 폴더명을 `.gitignore`로 설정.
- https://www.toptal.com/developers/gitignore 에서 window, python, visual studiocode 키워드를 입력하면 내 환경과 가장 최적화된 gitignore 코드들이 나온다. vscode에 복붙하여 commit-> github에 push하면 됨.

※ 주의

이미 커밋된 파일은 반드시 삭제를 해야 .gitignore이 적용되므로 `프로젝트 시작전에 미리 설정할 것`.


