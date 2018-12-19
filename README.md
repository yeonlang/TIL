# TIL

##### Today I Learn

# Day 01

### Git hub

```python
import requests

response='응답'
#123123
```



```bash
git config --global use.name 'Daehyun Kang'
git push -u origin master
```

### vscode 기본 terminal 변경

- `ctrl + shift + p`
- shell 검색 
- Select Default Shell
- Git Bash



### vscode 단축키

- ` ctrl + backtick ` : 터미널 보기



### bash

* ```bash 
  cd 주소		# 폴더이동
  cd ..		 # 이전폴더 이동
  mv *.txt day02/dummy/ # txt 확장자의 모든 파일을 day02/dummy 폴더로 이동
  ```

# Day 02

### import OS

* ```python
  os.chdir(r'url') #
  print(os.getcwd()) # 
  os.listdir('.') 
  # os.getcwd()로 불러온 것을 리스트형으로 보여준다.
  # 사용법은 for filename in os.listdir('.') 와 같이 사용한다.
  os.rename(filename, f'지원자_{filename}')
  #이름을 변경하는 함수 
  #{filename}에서 원래파일 이름을 가져온후 뒤에 지원자_를 붙인다.
  replace('바꾸고싶은 이름', '바꾸고 난 후의 이름')
  #사용법은 s.replace('abc','def')와 같다. s는 문자열변수이다.
  for filename in os.listdir('.'):
      new_filename = filename.replace('지원자_','합격자_')
      os.rename(filename, rename)
  #filename에 원래이름이 리스트로 저장되고 
  #new_filename에 지원자_->합격_자로 바뀐 이름이 리스트로 저장된다.
  #rename함수를 이용하여 filename을 new_filename으로 바꾸어준다.
  ```

### text 편집

* ```python
  open(파일이름, 파일열기모드) 
  # 그리고 close()가 붙어야 open()메소드가 정상적으로 종료된다. 
  with open()
  # close()를 사용하지 않아도 정상적으로 종료된다.
  
  open(파일이름, r) # 읽기모드로 파일을 연다. 읽어오는 것만 가능하다.
  open(파일이름, w) # 쓰기모드로 파일을 연다. 파일에 내용을 입력할 수 있다.
  open(파일이름, a) # 추가모드로 파일을 연다. 파일 내용의 마지막에 내용을 새로 추가한다.
  
  read() 메소드 - #내용 전체를 문자열로 반환해 준다.
  readline() 메소드 - #한줄씩 문자열로 반환해 준다.
  readlines() 메소드 - #모든 라인을 읽어서 리스트로 반환해 준다.
    
  ```

* ```python
  with open('This is SSAFY!','w',encoding='utf8') as f :
      f.write('This is SSAFY!, with 이용했다.')
  # ssafy.txt를 utf8 형식으로 열어보는 함수이다. 없을경우에는 ssafy.txt를 생성한 후 오픈한다
  # w:write, r : read, a :append 를 의미한다. 
  # This is SSAFY!, with 이용했다.를 텍스트 내용에 추가한다.
  ```

### 2일차 정리

##### Git 설정

* `git config --global user.name 'Daehyun Kang'`
* `git config --global user.email 'napsy001@gmail.com'`
* `git init` : git 초기화, git으로 관리하겠다!
* `git remote add origin 주소` : 원격 저장소 등록
  * `git remote set-url origin 주소`  : 원격 저장소 수정

##### Git 설정 및 Commit

* `git status` : 현재 폴더의 git 상태
* `git add .` : 현재 폴더의 변경사항들을 commit 하기 위해서 준비
* `git commit -m 'day 02 입니다.'` : commit, 변경 사항 저장 . 메시지는 자유작성 가능
* `git push -u origin master ` : remote로 등록된 원격 저장소 (remote repository) 
  * 이후에는 git push 만 입력해도 동작합니다.	



* Markdown 기록할 것입니다.
  * `typora` vs `vscode`

### 파일조작

* file write, read 활용해서 역순으로 저장

* ```python
  with open('SSAFY.txt','r', encoding='utf8') as f :
      lines = f.readlines()
      for line in lines :
          print(line)
  -------------------------------------------------------
  ssafy.txt
  1
  2
  3
  ```

* ```python 
  with open('SSAFY.txt','r', encoding='utf8') as f :
      lines = f.readlines()
      for line in reversed(lines) :
          print(line)
  -------------------------------------------------------
  ssafy_reverse.txt
  3
  2
  1
  6 5
  43 32
  21
  ```

* ``` python
  #예시 코드
  with open('SSAFY.txt','r', encoding='utf8') as f :
      lines = f.readlines()
      for line in lines :
          print(line)
  
  #1.한번에 처리
  with open('SSAFY.txt','r', encoding='utf8') as f :
      lines = f.readlines()
      with open('This is SSAFY!','w',encoding='utf8') as ff :
      ff.writelines(reversed(lines))      
      
  #2.read/write 분리처리
  with open('SSAFY.txt','r', encoding='utf8') as p :
      lines = p.readlines()
      lines.reverse()
  
  with open('This is SSAFY!','w',encoding='utf8') as pp :
      pp.writelines(reversed(lines))        
  ```

* csv를 만들어주는 프로그램   

  ```python
  lunch = {
      '횡성한우':'054-474-1235',
      '영덕대게':'054-485-1841',
      '영광굴비':'054-475-5689'
  }
  import csv
  
  with open('lunch.csv', 'w' , encoding = 'utf8', newline = '') as f:
      csv_writer =csv.writer(f) #f는 파일 내용
      for item in lunch.items():
          csv_writer.writerow(item)
      # for item in lunch.items(): # 리스트 [(key, value),...]
      #     f.write(f'{item[0]},{item[1]}\n')  
  ```

### 크롤링

* 네이버 실시간 랭킹 불러오는 프로그램  

  ```python 
  import requests
  import bs4
  
  response = requests.get('https://www.naver.com/').text
  soup = bs4.BeautifulSoup(response, 'html.parser')
  result1 = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_r')
  result2 = soup.select('div.PM_CL_realtimeKeyword_list_base span.ah_k')
  i=0
   for item in result2 :
       print(f'{result1[i].text} / {item.text}')
       i=i+1    
  ```

* 헤더파일을 추가하여 프로그램접근을 방지해놓은 곳에서 크롬을 통해 접속하는 것으로 착각하게 만든 프로그램

  ```python
  import requests
  import bs4
  
  h= {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
  }
  response = requests.get('https://www.melon.com/chart/index.htm',headers=h).text
  soup = bs4.BeautifulSoup(response, 'html.parser')
  print(response)
  ```

### 유용한사이트

* https://startbootstrap.com/template-categories/all/
* https://www.acmicpc.net/
* 플라스크

유용한 기능

ctrl + D

alt + 좌클릭



### HTML, CSS

* ``` HTML
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>HTML Practice</title>
          <style> 
              h1 , h3{
                  color: tomato;
              }
              h2{
                  color: blue;
              }
              #green {
                  color: green;
              }
              .yellow {
                  color: yellow;
              }
          </style>
      </head>
      <body>
          <!--이것은 주석입니다.-->
          <h1>이것은 h1 태그입니다.</h1>
          <h2>이것은 h2 태그입니다.</h2>
          <h3>이것은 h3 태그입니다.</h3>
          <h4 id="green">이것은 h4 태그입니다.</h4>
          <h5 class="yellow">이것은 h5 태그입니다.</h5>
          <h6 class="yellow">이것은 h6 태그입니다.</h6>
  
          <p style="color : pink;">
              이것은 p 태그입니다. 
              이것은 p 태그입니다. 
              이것은 p 태그입니다. <br>
              이것은 p 태그입니다. 
              이것은 p 태그입니다.
          </p>
  
          <ul>
              <li>리스트 1번째</li>  
              <li>리스트 2번째</li>
              <li>리스트 3번째</li>
          </ul>  
          <ol>
              <li>리스트 1번째</li>
              <li>리스트 2번째</li>
              <li>리스트 3번째</li>
          </ol>
  
          <div>
              <b>여기는 div입니다.</b>
              <i>여기는 div입니다.</i>
  
          </div>    
          
      </body>
  </html>
  ```

### 플라스크 설치

* bash에서 pip install flask

* ```python
  rom flask import Flask
  app = Flask(__name__)
  
  @app.route("/")
  def hello():
      return "Hello World!"
  ```

* ``` python
  from flask import Flask, render_template
  import random
  
  app = Flask(__name__)
  
  @app.route("/greeting/<string:name>")
  def greeting(name):
      return f'반갑습니다.{name}님'
  
  @app.route("/cube/<int:num>")
  def cube(num):
      cube =num**3 # == num * num * num 
      return f'{num}의 세제곱은 {cube}입니다.'
  
  @app.route("/lunch/<int:person>")
  def lunch(person) :
      menu = ['김치찌개', '된장찌개', '부대찌개', '재첩국', '미역국' ,'등심 스테이크', '함바그', '투움바 파스타' ,'로제 파스타']
      
      order = random.sample(menu,person)
      return str(order)
  
  @app.route("/html")
  def html():
        
      return '''<h1>이것은 h1 입니다.<h1>
          <p>여기는 p 입니다. </p>
          '''
     
  
  @app.route("/html_file")
  def html_file() :
      return render_template('html_file.html')
  
  @app.route("/hi/<string:name>")
  def hi(name) :
          return render_template('hi.html', name = name)
  
  @app.route("/fake_naver")
  def fake_naver():
          return render_template('fake_naver.html')
  
  ```

* ``` python
  
  <h1>Naver</h1>
  <form action="https://search.naver.com/search.naver">
      <input type="text" name="query">
      <input type="submit">
  </form> 
  
  <h1>Daum</h1>
  <form action="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&">
      <input type="text" name="q">
      <input type="submit">
  </form> 
  
  ```

* 