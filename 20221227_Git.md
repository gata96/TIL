# CLI (Command Line Interface)
> ### Command를 Line 별로 타이핑하며 유저와 소통하는 방식

    - 인터페이스 : 유저와 하드웨어 사이의 경계
    - 폴더나 파일 등 내가 눈으로 보고싶으면 명령(Command)을 하고 그 결과를 읽어내야 한다. 
    - 불편한 것이 아니라 GUI와 사용법이 다른 것일 뿐. 익숙해지면 원리는 같다. 리눅스 아님. 윈도우임.


<br>

## GUI와의 차이점
<br>

> ### GUI (Graphic User Interface)
    -위도우에서 흔히 볼 수 있는 그래픽 기반의 인터페이스
    -딱히 명령을 안해도 폴더, 파일이 눈에 직관적으로 보인다.

- 터치 인터페이스 ; 스마트폰
- 키보드, 마우스 인터페이스 ; 컴퓨터
> 

<br>

|명령    | GUI    | CLI |
| ------|---------|------|
|파일열기| 더블클릭| ls |  #ls: list(목록)
|새폴더 생성|오른쪽마우스|mkdir 폴더명| #디렉토리 생성(make directory)
|폴더열기| 더블클릭|cd|
|상위로 이동|뒤로가기|cd ..| #cd 치고 띄어쓰기 있다.
|현재 디렉토리|.|.|
|새파일 생성|오른쪽마우스| touch 파일명|
|파일삭제|delete| rm 파일명|
|폴더삭제|delete| rm -r 폴더명|

<br>

- *rm 폴더명*
   ```python
   cannot remove 'b': is a directory 
   ```

'rm 폴더명'으로 폴더를 삭제하려고 할 시, GUI에서는 노이로제 소리로 막아주지만, CLU에서는 위와 같은 메세지로 막아준다.<br> 마치 *'진짜 삭제할 거야? 확실해?'* 라고 묻는 느낌.

<br>

- `$` : 명령을 입력할 준비가 되었다는 사인이므로 타이핑 할 때는 $ 안써도 된다.
- ~: home
- pwd (print working directory)

# Git
### **git은 분산 버전관리 시스템 중 하나이다.**
<br>

> 분산 버전관리 시스템 : 로컬 버전 관리
- 버전관리: 작업(CRVD한 파일)을 add하고 commit하는 것
    - CRVD: c생성,R읽기,V수정,D삭제-> 파일이 변경되는 것은 C,V,D밖에 없다.

- 문서는 하나지만 버전이 기록되어 있으면, 이전 시점을 조회하거나 복원할 수 있다.
- ex) 카카오톡 버전 업데이트
- Git 덕분에 구글 1버전당 1.5GB이지만 1000만개의 버전을 전체 다운 받으면 25GB 밖에 안됨.
- Git이 초반에는 구글의 슈퍼 짱 개발자들도 분산 버전관리 시스템에 대해 이해하지 못했다. 지금은 세계적인 분산 버전 시스템임.
- 중앙버전관리시스템과 달리 로컬(or 유저)가 버전을 기록하고 관리한다.

## 버전관리 방법


 1. Working Directory 단계 

- 로컬 저장소 생성
- 문서를 기록하거나 수정한다. (Write)
- git init 이라는 명령어 사용
- `$` git status로 Git 저장소에 있는 파일의 상태를 확인할 수 있다.)
- 1단계까지만 하고 `$` git status를 확인하면 이런 메세지 창 뜬다. add까지 하고 status확인하라는 뜻.
```python
nothing added to commit but untracked files present (use "git add" to track)
```

<br>

**↓ `$` git add 파일명**

<br>
    
2. Staging Area 단계 
- 1단계의 변경된 내용의 파일들을 모은다.
- commit 전, 변경된 파일들 목록(Add)
- `$` git status로 상태 확인

<br>

**↓  `$` git commit -m '커밋메세지'**  

<br>

3. Repository 단계 
- 커밋하여 New 버전 기록을 남긴다. (Commit)
- 커밋메세지는 변경사항을 잘 나타낼 수있도록 명확하게 표현할 것.
- `$` git log로 Repositoy의 상태 확인

<br>

> ### `$` git status
- 1과 2단계에서 쓸 수 있으며, 파일 상태를 확인 할 수 있다.

```python
'Untracked filed'
# 트래킹 되지 않은 파일들.txt를 만들었지만, add를 하지 않음

'Changes to be committed'
# 커밋 될 변경사항들. txt만들고 add함.

'nothing to commit, working tree clean'
# 모두 add, commit한 경우. 
# working tree clean: 지난번에 버전 기록한 거 중에 수정한게 없고(파일의 변경사항이 없고), nothing to commit: add한 것도 없어.

'Changes not staged for commit'
# 커밋된 적 있는 .txt 파일을 수정한 상태.

```

# Summary

저장소 처음 만들때
```bash
git init
```

버전을 기록할 때
```bash
git add .
git commit -m '커밋메세지'
```

상태 확인 할 때
```bash
git status: 1통
git log : 커밋확인
```

원격저장소 활용하기
```bash
git remote add origin URL
```

push/pull
```bash
git push origin master
git pull origin master
```
