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
  c9 ~/.bashrc
  exec $SHELL
  
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

* `git clone https://github.com/yeonlang/TIL.git                                 ` : 클론을 만든다

* `mv TIL/ Daehyeon/`:TIL의 이름을 바꾼다(혹은 폴더를 이동한다)

   



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



# Day03



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
  #플라스크 서버생성 
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/")
  def hello():
      return "Hello World!"
  
  #bash에서 플라스크 실행
  FLASK_APP=hello.py flask run
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

* ```python
  #파이썬 구동함수 
  #로또 당첨페이지에서 자료를 긁어온다.
  @app.route("/lotto/<int:num>")
  def lotto(num):
          url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
          response = requests.get(url)
          lotto = response.json()
          
          winner = []
          for i in range(1,7):
                  winner.append(lotto[f'drwtNo{i}'])
  
          bonus = lotto['bnusNo']
  
          return render_template('lotto.html', w=winner, b=bonus, n=num)
  # html 구현함수
  <h1>{{ n }}회 당첨 번호는?</h1>
  <h2>당첨 번호 : {{ w }}</h2>
  <h2>보너스 번호 : {{ b }}</h2>
      
      
      
  ```

# Day 04

* 딕셔너리 활용

* ``` python
  lunch = {
      '중국집' : '02-316-5554' ,
      '양식집' : '054-563-1331' ,
      '한식집' : '053-525-4379' ,
  }
  print(lunch)
  
  # 1. 딕셔너리 내용 생성
  dinner = dict(중국집='02-123-123')
  
  # 2. 딕셔너리에 내용 추가하기
  lunch['분식집'] = '053-123-123'
  
  # 3. 딕셔너리 내용 가져오기
  print(lunch['중국집']) #=> '02-316-5554'
  
  # 4. 딕셔너리 반복문 활용하기
  for key in lunch:
      print(key,end=' ')
      print(lunch[key])
  
  idol = {
      'bts' : 
       {
          '지민' : 24,
          'RM' : 25,
      }
  }
  idol['bts'] #=> { '지민' : 24, 'RM', 25}
  idol['bts']['RM'] #=> 25
  
  # key 만 가져오기
  for key in lunch.keys():
      print(key)
  
  # value만 가져오기 : .values()
  for value in lunch.values() :
      print (value)
  
  # item(key, value) 가져오기 : .items()
  # lunch.items) #=> [('중식','02'), ... ]
  for item in lunch.items()
      print(item[0], item[1])
  
  # item을 분리해서 가져오기
  for key, value in lunch.items()
      print(key, value)
  
  # 2개 = 자료형(list, tuple, ...) 길이 2
  a , b , c = (1,2,3)
  print(a)
  print(b)   
  
  #이단 딕셔너리 활용
  scores = {
      'a' : {  
          '수학' : 80,
          '국어' : 90,
          '음악' : 70,
          },
      'b' : {  
          '수학' : 80,
          '국어' : 90,
          '음악' : 100,
          }
  }
  
  total_score = 0
  count = 0
  
  for person_score in scores.values() : #=> [{ '수학' : 80, '국어' : 90, '음악' : 70} ,{'수학' : 80,'국어' : 90,'음악' : 100}]
      # person_score #=> { '수학' : 80, '국어' : 90, '음악' : 70}
      # person_score.values() #=>  [80, 90, 70]
      for subject_score in person_score.values():
          # 1번째 시행 일때
          # subject_score #=> 80
          total_score += subject_score
          count += 1   
  print(total_score/count)
  ```

* ```python
  # 문제 1 평균 구하기
  score = {
      '수학' : 80,
      '국어' : 90,
      '음악' : 100,
  }
  
  # #풀이 1
  # add=0
  # num=0
  
  # for value in score.values():
  #     add = add + value
  #     num = num + 1
  # print(add/num)
  
  #풀이 2
  total_score = sum(score.values()) #=> sum([80,90,100]) = 270
  avg_score = total_score / len(score) #=>270 / 3
  print(avg_score)
  ```

* ```python
  # 문제 2 반 평균을 구하시오
  scores = {
      'a' : {  
          '수학' : 70,
          '국어' : 90,
          '음악' : 100,
          },
      'b' : {  
          '수학' : 80,
          '국어' : 90,
          '음악' : 100,
          }
  }
  
  num = 0
  total = 0
  
  for key in scores :
      for mem in scores[key] :
          total = total + scores[key][mem]
          num = num + 1
  print(total/num)    
  # #풀이2    
  # a_total = sum(scores['a'].values())
  # b_total = sum(scores['b'].values())
  
  # print((a_total+b_total)/(len(scores['a'])+len(scores['b'])))
  ```

* ```python
  import random
  
  ssafy = {
      "location": ["서울", "대전", "구미", "광주"],
      "language": {
          "python": {
              "python standard library": ["os", "random", "webbrowser"],
              "frameworks": {
                  "flask": "micro",
                  "django": "full-functioning"
              },
              "data_science": ["numpy", "pandas", "scipy", "sklearn"],
              "scrapying": ["requests", "bs4"],
          },
          "web" : ["HTML", "CSS"]
      },
      "classes": {
          "gm":  {
              "lecturer": "junwoo",
              "manager": "pro-gm",
              "class president": "엄윤주",
              "groups": {
                  "1조": ["강대현", "권민재", "서민수", "이규진"],
                  "2조": ["박재형", "서민호", "윤종원", "이지현"],
                  "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                  "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
              }
          },
          "gj": {
              "lecturer": "change",
              "manager": "pro-gj"
          }
      }
  }
  
  # 난이도* 1. 지역(location)은 몇개 있나요? : list length
  # 출력예시)
  # 4
  
  print(len(ssafy['location']))
  
  # 난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
  # 출력예시)
  # false
  count = False
  for library in ssafy['language']['python']['python standard library'] :
      if 'requests' == library :
          count = True
  if count :
      print("requests 라이브러리가 존재합니다.")
  else :
      print("requests 라이브러리가 존재하지 않습니다.")        
  
  comp = ssafy['language']['python']['python standard library']
  print('os' in comp) #==> os가 comp딕셔너리 내부에 존재하는가?
  
  # 난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
  # 출력예시)
  # 엄윤주
  
  print('gm 반의 반장은 ' + ssafy['classes']['gm']['class president'] + ' 입니다.')
  
  # 난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
  # 출력 예시)
  # python
  # web
  
  
  for key in ssafy['language'].keys():
      print(key)
  
  # 난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
  # 출력 예시)
  # change
  # pro-gj
  
  for key in ssafy['classes']['gj'].values():
      print(key)
  
  # 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
  # 출력 예시)
  # flask는 micro이다.
  # django는 full-functioning이다.
  
  for f_name, f_expain in ssafy['language']['python']['frameworks'].items():
      print(f'{f_name}는 {f_expain}이다.')
  
  # 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
  # 출력예시)
  # 오늘의 당번은 하창언
  
  c = random.choice(ssafy['classes']['gm']['groups']['4조'])
  print(f'4조 오늘의 당번은 {c}입니다.')
  v = []
  for t in ssafy['classes']['gm']['groups'].values() :
      v.extend(t)
  print(f'1반 오늘의 당번은 {random.choice(v)}입니다.')
  ```

# Day05

bash