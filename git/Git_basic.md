# Git&Github

## Git에 내 정보 설정

* `git config --global user.name 'Daehyeon Kang'`
* `git config --global user.email 'naspy001@gmail.com'`

## Git repo 를 처음 생성한 경우

* `git inin` : git 초기화, 지금 폴더를 git으로 관리하겠다!	

  (관리하려는 폴더 안에서 입력)

* `git remote add origin 주소` : 원격 저장소(remote repository)주소 등록

  * `git remote set-url origin 주소` : 

    원격 저장소(이 저장소 중 하나가 git hub의 개인 웹) 수정

## Git repo clone 한 경우

* `git clone 주소 [폴더이름]` 

  : 이 주소로 부터 내용 내려받기 [] 안의 내용은 입력을 하여도 하지 않아도 무관

  * 이 경우에는 `git init`, `git remote add origin 주소 ` 를 하지 않아도

    이미 설정이 되어있다.

## GIt Commit*Push

* `git status`  : 현재 폴더의 git 상태 확인

* `git add .`  : 현재 폴더의 변경사항들을 commit하기 위하여 준비

* `git commit -m 'D04 | 190107 AM | Git & CLI' ` 

* `git push -u origin master` : remote로 등록된 원격 저장소에 commit한 것들 올리기

  * 이후에는 git push  만 입력해도 동작합니다.

  * 이 컴퓨터에서 최초 push 인 경우 로그인창이 뜨게 됩니다.

## Git Pull

* `git pull`  : GitHub에 올라가 있는 내용들 , 즉 commit들을 내려받는것.
* 아침에 오자마자 `git pull` 한번 하고 시작합시다!



## Git&GitHub 재설정

```bash
#Git 이름, 이메일 재설정 
git config --global user.name 'Daehyeon Kang'
git config --global user.email 'naspy001@gmail.com'

#로그인 정보 초기화
git credential reject
protocol=https
host=github.com 

```

## 순서도

```bash
git clone {주소} {변경할 이름} #{}은 제외하고 입력

git remote add origin #클론으로 입력받을 경우 생략가능

git credential reject
protocol=https
host=github.com #기존 설정된 로그인 계정 취소

git push 
# 새로운 계정을 등록하기위해 푸쉬를 누른 후 새로 로그인을 해준다.

git config --global --list
#현재의 유저 네임과 이메일 주소가 뜬다.

git config --global user.name 'Daehyeon Kang'
git config --global user.email 'naspy001@gmail.com'
#커밋을 할 시에 들어가는 정보를 수정해준다.

# +)git log : 로그를 보여준다 Q로 빠져나올 수 있다.
```

