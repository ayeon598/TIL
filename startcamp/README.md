# SSAFY_STARTCAMP
## 2025.01.15
### ordered 리스트
1. 1번
2. 엔터 눌러보세요
   1. tab 누르면 2-1번
   2. 2-2번
3. 3번
### unordered 리스트
+ -기호 또는 +기호 또는 *기호
+ 엔터
  + tab키 누르기
+ unordered 리스트
### 체크리스트 만들기
- [x] 토스트
- [x] 당근
- [ ] 양파
- [ ] 라면
### 코드블럭 백틱 3번
```python
print('hello world')
```
### 링크 url 걸기
[네이버](http://www.naver.com)
### 이미지 걸기
![고양이](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDExMTJfMjQw%2FMDAxNzMxMzgwOTkzODA1.WEB78UeJ6swaPE-7Cx7CDHob84DlKIKyu-UtgBrUiu8g.IVxbdCcSY12-5HGbxnGcgrZhSnwoqvDAnRzs3J6iGp0g.PNG%2FKakaoTalk_20241112_000914392.png&type=a340)
### 이미지 걸기2
![강아지](./dog.jpg)
### 굵게 표현하기
__굵은 글씨__ (언더바 2번)
중간에 **굵은 글씨**를 넣기
### 기울기 표현하기
_기울기 글씨_ (언더바 1번)
중간에 *기울기 글씨*를 넣기
### 굵게 및 기울임
___굵게 및 기울임___ (언더바 3번)
중간에 ***굵기 및 기울임***을 넣기
### 취소선
~~취소선~~ (물결2개)
### 수평선
---
### markdown 왜 배울까?
github에 프로젝트 올릴때 README.md 파일에 활용
---
### GUI(Graphic User Interface) [<-> TUI(Text User Interface)]
좌클릭 두번으로 디렉토리를 열 수 있다.
### CLI(Command Line Interface) == TUI(이 말은 잘 안 씀.)
bash를 열어 경로를 바꿔서 열 수 있다.
* cd practice/ : 경로에 practice 추가
* ls
### interface
대상을 제어하는 수단(리모컨)
### Window OS의 Interface
* GUI = "Windows Shell"
* CLI = "Power shell", "명령프롬프트(cmd라고 부름)"
### Linux OS의 Interface
* GUI = "GNOME"
* CLI = "Bash"
### Bash 왜 쓸까?(Bash 장점)
Bash가 편해서(Tab키 자동완성 기능)
### Git을 다룰 때 Interface
* GUI = "Github Desktop", "소스트리"
* CLI = "git bash" - 많이 쓸 예정
### git 쓸 때 GUI로 다뤄야할까? CLI로 다뤄야 할까?
1. GUI 장점
   1. 보기 편하다. 친숙하다.
   2. 복잡한 분석(Graph 같은 것을 훨씬 보기 좋다.)
2. CLI 장점
   1. 빠르다.(Commit 명령어 2~3초면 끝)
   2. 20년 전에 배웠으면, 현재도 쓰고 있고, 미래에도 쓸 예정(빠르고 변함이 없다.)
3. 결론 : 둘 다 써야하지만 대부분 CLI 쓸 예정
---
### VScode : IDE?
NO! VScode = 텍스트 에디터(익스텐션을 추가해서 마치 IDE처럼 사용)
### IDE
* Python : PyCharm, 쥬피터노트북
* C# : Visual Studio
* Java : IntelliJ
---
### 민지W(Minnimal GNU for Windows)
* 윈도우환경에서 리눅스에 쓰이는 툴들을 쓸 수 있게 가볍게 만든 프로젝트
### 리눅스
* 리눅스는 항상 HOME 디렉토리 : ~
* cd ~ : 홈 디렉토리
* cd - : 뒤로가기
* cd .. : 상위 디렉토리
### 기본 명령어
* touch : 파일 생성 (touch a.txt)
* mkdir : 폴더(디렉토리) 생성 (mkdir practice2)
* start : 파일 열기 (start a.txt)
* rm : 삭제 (rm a.txt)
* cp : 파일 복사 (cp dog.jpg dog2.jpg)
* cp -r : 폴더 복사 (cp -r practice/ practice2)
* cd ~/Desktop/practice/practice3 : 절대 경로
* cd ./practice3 : 상대 경로(./ or ../)
* ls : 안에 생성되어 있는 파일 및 폴더 알려줌
---
### git : 분산관리시스템
* github : 원격저장소 - 온라인 상에 프로젝트를 올리는 것
* git : 로컬저장소 - 내 컴퓨터에서 파일을 관리하는 것
* GIT -> GITHUB : push
* GIT <- GITHUB : pull
* git bash에서 git init 하면 master라고 뜸. 이 때 github branch 이름이랑 같아야 함.
* git init : git 시작(git 폴더 생성)
* rm -rf.git : .git 폴더 삭제
* git config --global user.name "이름"
* git config --global user.email "이메일"
* git push 이후 자리 옮겼을 때 제어판의 windows 자격 증명 -> 일반 자격 증명에서 github 삭제
* git commit -m "메시지명" : repository에 올리기
* git log : repository 작업 파일 확인(커밋 되어 있는지 확인) - q 입력하면 나올 수 있다.
### git의 3가지 영역(책 71p~)
1. Working Directory
   * git add . : Working Directory -> Staging Area (Staging Area에 올리기), 변경사항이 생길 때만 add가 됨.
2. Staging Area
   * git status : Staging Area 작업 파일 확인
   * git commit : Staging Area -> Repository
3. Repository
   * 실질적인 버전 관리
---
## 2025.01.16
### GIT Bash
* shift + insert : 붙여넣기
* Ctrl + shift + c : bash 안에서 복사하기
### GIT과 GITHUB 연결 : git remote
* git remote add origin(별칭) github링크(url) : url repository에 별칭 부여
* git remote -v : 별칭 확인
* git push origin +master : 푸시
* git remote rm origin(별칭) : 별칭 삭제
### clone과 pull의 차이가 뭘까?
* clone : 내가 새로운 환경에서 처음 다운로드
   * git clone github링크(url)    
* pull : push나 clone을 전에 진행한 후에 다운로드
   * git pull origin +master
### git ignore
* .gitignore 파일 생성
* .gitignore에 올리고 싶지 않은 파일 이름들을 써주면 됨.
### .gitignore 파일을 왜 만들까?
* 용량이 크거나, 보안상 문제가 있거나 청구결제 관련된 api_key 같은 파일을
  add 하지 않기 위해(staging area에 올리지 않기 위해)
* gitignore 파일 생성 -> add 하지 않을 파일명이나 디렉토리명 작성, 저장
### git push 이후 자리 옮겼을 때 제어판의 windows 자격 증명
* 일반 자격 증명 에서 github 삭제하기
---
## git 심화
### git commit 메시지 수정하기
* git commit 까지 완료한 후에 : git commit --amend (vim 접속됨)
* vim에서 esc :q! 입력 : 강제 종료(저장 안 됨), esc :wq 입력 : 강제 저장 후 종료
### commit을 새로 생성하지 않고 전체 수정하기
* git add. -> git commit --amend : 메시지, 날짜, 파일(vim 수정) 저장
### git revert
* 특정 commit을 없었던 일로 만듦
   1. git log --oneline : 해시값(메시지 앞에 있는 문자들-노란색) 확인
   2. git revert 해시값
### git reset
* 특정 commit으로 되돌리기
   1. git log --oneline : 해시값(메시지 앞에 있는 문자들-노란색) 확인
   2. git reset --hard 해시값
### git reflog
* 이때까지 한 전체 commit을 모두 확인 가능(과거 commit 기록)
  * git reflog
### git add 취소하기
* staging area에 있는 작업을 working directory로 옮기기
   1. 이전에 했던 commit이 없는 경우
      * git rm --cached 파일명
   2. 이전에 했던 commit이 있는 경우
      * git restore --staged 파일명
---