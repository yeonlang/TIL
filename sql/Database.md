# Database

[TOC]

## Introduction 

**데이터베이스란?** 

SQL언어로 조작을 할 수 있는 체계화된 데이터의 모임.

예)  RDBMS(관계형 데이터 베이스 관리 시스템): 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템.  대표적으로 오픈소스 RDMBS 인 MySQL, SQLite, PostgreSQL와 ORACLE, MS SQL 등이 있음.

> 여러 사람에 의해 공유되어 사용될 목적으로 통합하여 관리되는 데이터의 집합을 말하는 개념이다. 줄여서 DB라고도 하며, 특정 다수의 이용자들에게 필요한 정보를 제공한다든지 조직 내에서 필요로 하는 정보를 체계적으로 축적하여 그 조직 내의 이용자에게 필요한 정보를 제공하는 정보 서비스 기관의 심장부에 해당된다.

**SQLite**

서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 구글 안드로이드 운영체제에 기본적으로 탑재댄 데이터베이스이며 임베디드 소프트웨어에도 많이 활용되고 있다. 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이므로 자유롭게 사용이 가능하다.



### 기본 용어 정리

**스키마(scheme/schema)**

데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조. 데이터베이스의 구조와 제약조건에 관련한 전반적인 명세를 기술하였음. 이를 바탕으로 테이블 등을 생성 할 수 있음.



**테이블**

- 열(column): 각 열에는 고유한 데이터 형식이 지정된다. Integer, text, null 등
- 행(row), 레코드: 테이블의 데이터는 행에 저장된다. 즉 user 테이블에 4명의 고객정보가 저장되어 있으며, 행은 4개가 존재한다.
- 기본키(Primary Key): 각 행(레코드)의 고유값으로 Primary Key로 불린다. 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.



### SQL의 개념

SQL(Structured Query Langauage)는 관계형 데이터 베이스 관리 시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.RDBMS에서 자료의 검색과 관리, DB의 스키마 생성과 수정, 데이터벵스 객체 접근 조정 관리를 위해 고안되었다.



**SQL의 문법**

| 언어                  | 정의                                                         | 예시                            |
| --------------------- | ------------------------------------------------------------ | ------------------------------- |
| 데이터 정의 언어(DDL) | 데이터를 정의하기 위한 언어. 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어. | CREATE, DROP, ALTER             |
| 데이터 조작 언어(DML) | 데이터를 저장, 수정 삭제, 조회등을 하기 위한 언어            | INSTER, UPDATE, DELETE, SELECT  |
| 데이터 제어 언어(DCL) | 데이터 베이스 사용자의 권한 제어를 위한 사용되는 언어        | GRANT, REVOKE, COMMIT, ROCKBACK |



## C9에서 SQLite 조작하기

**SQLite 실행 및 SELECT문 실행하기**

```bash
#C9에 내장되어있는 SQLite 실행하기
harrylee0810:~/workspace/flask/sql $ sqlite3

#실행하면, 다음과 같은 코드가 실행된다.
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";" 

#examples라는 테이블을 생성
sqlite> .mode csv
sqlite> .import hellodb.csv examples

#SELECT문은 데이터베이스에서 특정한 행을 출력한다.
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

#header를 on하고, 모드를 csv가 아닌 column으로 변경해보자
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT*FROM examples;
id          first_name  last_name   age         country     phone        
----------  ----------  ----------  ----------  ----------  -------------
1           길동      	홍         600         충청도   	010-2424-1232

#sqlite 종료하기
#명령어 앞에 .을 쓰는것은 SQL의 언어가아니라 sqlite를 조작하는 명령어임.
sqlite> .exit
```



**Database 생성하기**

```bash
#데이터 베이스 생성하기(sqlite3는 확장자는 제한이 없음. tutorial.sqlite3 라는 파일을 생성)
harrylee0810:~/workspace/flask/sql $ sqlite3 tutorial.sqlite3

SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"

#.databases: 생성된 데이터베이스의 목록을 열어줌.
sqlite> .databases

seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/flask/sql/tutorial.sqlite3         
```



**Table 생성**

```sqlite
CREATE TABLE table명(
column1 datatype PRIMARY KEY,
column2 datatype
...
);
```

실습문제) classmate라는 테이블을 생성해보자!

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
classmates
```

sql의 구조는 개행문자를 인식하지 않음. `;` 를 입력해야 명령어가 종료됨. otherwise, 엔터를 처도 한줄로 인식함



**Table과 Database의 관계**

하나의 데이터베이스안에는 여러개의 테이블이 존재할 수 있음.

Movie recomendation (DB)

- users (Table 1) 
- movies (Table 2)
- movie_rates (Table 3)



**Datatype**

SQLite는 동적 데이터 타입으로 기본적으로 affinity에 맞게 들어간다. BOOLEAN은 정수 0,1으로 저장된다.

| Class   | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| NULL    | NULL values mean missing information or unknown.             |
| INTEGER | Integer values are whole numbers (either positive or negative). An integer can have variable sizes such as 1, 2,3, 4, or 8 bytes. |
| REAL    | Real values are real numbers with decimal values that use 8-byte floats. |
| TEXT    | TEXT is used to store character data. The maximum length of TEXT is unlimited. SQLite supports various character encodings. |
| BLOB    | BLOB stands for a binary large object that can be used to store any kind of data. The maximum size of BLOBs is unlimited. |



**Table 및 schema 조회**

 `.tables` : 테이블 목록 조회

`.schema tables`  : 특정 테이블의 Schema 조회 

```sqlite
sqlite> .schema classmates
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT
);
sqlite> 
```



**Table 삭제(Drop)**

 `DROP TABLE table이름;`  : 특정 table 삭제. 삭제 후, `.tables` 명령어를 실행하면 삭제유무를 확인 할 수 있음.

```sqlite
sqlite> DROP TABLE classmates;
sqlite> .tables
```

`ctrl+L` : sql 터미널 정리하기



실습문제) classmates라는 테이블을 생성해보자!

```SQLITE
sqlite> CREATE TABLE classmates (
   ...> id INT PRIMARY KEY,
   ...> name TEXT,
   ...> age INT,
   ...> adress TEXT
   ...> );
sqlite> .tables
classmates   
```



## CRUD

### 1. 데이터 생성 (Create)

**data 추가(INSERT)**

특정 table에 새로운 행을 추가하여 데이터를 추가 할 수 있습니다.

```sqlite
INSERT INTO table명(column1, column2, ...)
VALUES(value1, value2, ...)
```



실습문제)  classmates 테이블에 이름은  홍길동, 나이는  23인 데이터를 넣어보고 SELECT문으로 확인해보자.

```sqlite
sqlite> INSERT INTO classmates(name, age)
   ...> VALUES(홍길동, 23);
 
sqlite> SELECT*FROM classmates;
            홍길동   23         
```



columns 이름은 생략 가능하며, 스키마의 구조에 맞게 VALUES()안에 연속적으로 데이터를 입력할 수 도 있음.

```SQLITE
sqlite>  INSERT INTO classmates VALUES(2, '홍길동', 50, '서울'); 
sqlite> .headers on
sqlite> .mode column

sqlite> SELECT*FROM classmates;
id          name        age         address   
----------  ----------  ----------  ----------
            홍길동   		23                    
2           홍길동   		50          서울    
```



위의 구조가 괜찮은가? 첫번째 필드의 주소가 비어있는걸 알 수 있음. 따라서, 컬럼이 공백이 되지 않게 수정해보자



**TALBE 설정 변경**

```sqlite
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
```

기본키의 값이 자동으로 생성될 수 있게, `id INTEGER PRIMARY KEY AUTOINCREMENT,` 를 입력하였으며, 나머지의 값은 공백이 되지 않도록, `NOT NULL` 을 입력하였음. 

이제 다시, 이름, 나이 값만 입력하면, 에러가 뜨는 것을 알 수 있음.

```sqlite
sqlite> INSERT INTO classmates(name, age) VALUES('홍길동',23);
Error: NOT NULL constraint failed: classmates.address
```

기본키(id)가 자동으로 생성되게 설정하였기 때문에, id값을 입력하지 않아도 데이터 추가가 가능하다.

```sqlite
sqlite> INSERT INTO classmates(name, age, address) VALUES('홍길동',50,'구미');
sqlite> SELECT * FROM classmates;
id          name        age         address   
----------  ----------  ----------  ----------
1           홍길동   50          구미    
```

id 값을 VALUE를 넣을경우 에러가 발생한다!



### 2. 데이터 읽기 (Read)

**data가져오기(SELECT)**

전체 데이터 갖고 오기

```SQLITE
sqlite> SELECT * FROM classmates;
```

특정한 table에서 원하는 데이터만 갖고오기 

```sqlite
sqlite> SELECT id,name FROM classmates;
id          name      
----------  ----------
1           홍길동 
2           홍길동 
3           홍길동 
4           진민재 
```

특정한 table에서 원하는 column의 데이터만 갖고오는데, 위에서부터 2개만 갖고오기!

```SQLITE
sqlite> SELECT id,name FROM classmates LIMIT 2;
id          name      
----------  ----------
1           홍길동 
2           홍길동 
```

위 2개를 생략하고 그다음 3개 갖고오기

```SQLITE
sqlite> SELECT id,name FROM classmates LIMIT 3 OFFSET 2;                                                    
id          name      
----------  ----------
3           홍길동 
4           진민재 
5           권민재 
```

조건 적용하기

```SQLITE
SELECT 컬럼명 FROM 테이블명 WHERE column=value
```

주소가 대구인 학생에 대한 데이터만 갖고오기

```sqlite
sqlite> SELECT id,name FROM classmates WHERE address="대구";
id          name      
----------  ----------
8           이규진 
9           강대현 
10          송현우 
11          양도혁 
```



### 3. 데이터 수정 (Update)

특정한 table에 특정한 레코드를 수정할 수 있습니다.

```SQLITE
UPDATE 테이블명 SET column1=value1, column2=column2,.... WHERE condition
```



실습문제) classmates 테이블에 id가 4인 레코드를 수정해보자 이름을 홍길동으로 주소를 제주도로 변경합시다.

```sqlite
sqlite> UPDATE classmates
   ...> SET name="홍길동", address="제주도"
   ...> where id=4;
sqlite> SELECT * FROM classmates;
id          name        age         address   
----------  ----------  ----------  ----------
1           홍길동   50          구미    
2           홍길동   50          구미    
4           홍길동   28          제주도 
5           권민재   27          수원    
...   
12          이지현   24          옥계    
13          조영현   24          구미    
```



### 4. 데이터 삭제 (Delete)

특정한 table에 특정한 레코드를 삭제 할 수 있습니다.

```sqlite
DELETE FROM 테이블명 WHERE 조건문
```



실습문제) 중복이 불가능한 값인 id(Unique한) 를 기준으로 id가 3번인 데이터를 삭제해보자

```sqlite
sqlite> DELETE FROM classmates WHERE id=3;
sqlite> SELECT * FROM classmates;                                                             
id          name        age         address   
----------  ----------  ----------  ----------
1           홍길동   50          구미    
2           홍길동   50          구미    
4           진민재   28          고령    
5           권민재   27          수원    
6           이현수   30          부산    
7           서민호   26          구미    
```



AUTOINCREMENT 속성을 통해 자동으로 id값을 입력하였음. 그런데 위의 예시처럼 id값이 3인경우에 데이터를 추가한다면? 

아래와 같이, id = 3은 비워두고, 밑에서 채워나가는 형태가 만듦어짐

```sqlite
sqlite> INSERT INTO classmates (name, age, address) VALUES ('조영현',24,'구미');      
sqlite> SELECT * FROM classmates;
id          name        age         address   
----------  ----------  ----------  ----------
1           홍길동   50          구미    
2           홍길동   50          구미    
4           진민재   28          고령    
5           권민재   27          수원    
....
12          이지현   24          옥계    
13          조영현   24          구미   
```



### 5. WHERE, expression

csv 파일을 임포트 해오자.

```sqlite
sqlite> .mode csv
sqlite> .import users.csv users
```

user.csv 파일을 이용해서 users라는 테이블을 만들겠다!

지금의 스키마는 모든 내용이 TEXT로 되어 있으므로  테이블을 삭제한 후, 스키마를 다시 설정해야함

```SQLITE
sqlite> .schema users
CREATE TABLE users(
  "id" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "age" TEXT,
  "country" TEXT,
  "phone" TEXT,
  "balance" TEXT
);
sqlite> DROP TABLE users;
sqlite> CREATE TABLE users (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> first_name TEXT NOT NULL,
   ...> last_name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> country TEXT NOT NULL,
   ...> phone TEXT NOT NULL,
   ...> balance INT NOT NULL
   ...> );
sqlite> .schema users
```



**where 심화**

users에서 age가 30이상인 사람만 가져온다면?

```SQLITE
sqlite> SELECT * FROM users WHERE age>=30;
```

users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 가져온다면?

```sqlite
sqlite> SELECT age, last_name FROM users WHERE age>=30 and last_name="김";
```

users에서 계좌 잔액(balance)이 가장 높은 사람과 액수는?

```sqlite
sqlite> SELECT first_name, MAX(balance) FROM users;
first_name  MAX(balance)
----------  ------------
순옥      1000000     
sqlite> SELECT first_name, MIN(balance) FROM users;                                     first_name  MIN(balance)
----------  ------------
우진      150         
```

users에서 30살 이상인 사람의 계좌 평균 잔액은?

```sqlite
sqlite> SELECT AVG(balance) FROM users where age>=30;
AVG(balance)    
----------------
153541.425120773
```

users 에서 나이가 20대인 사람?

```SQLITE
sqlite> SELECT * FROM users WHERE age LIKE '2%';
```

LIKE는 패턴을 찾아서 값을 비교해서 찾음.

**WHERE column LIKE ‘’**

| 형태   | 설명                                         |
| ------ | -------------------------------------------- |
| 2%     | 2로 시작하는 값                              |
| %2     | 2로 끝나는 값                                |
| %2%    | 2가 들어가는 값                              |
| _2%    | 아무값이나 들어가고 두번째가 2로 시작하는 값 |
| 1__    | 1로 시작하고 4자리인 값                      |
| 2\_%_% | 2로 시작하고적어도 3자리인 값                |



**Expression**

다음 표현은 레코드의 갯수를 반환합니다.

```sqlite
sqlite> SELECT count(*) FROM users;
COUNT(*)  
----------
1001      
```

다음 표현식은 기본적으로 숫자(INTEGER)일때만  가능하다.



**정렬(ORDER)** 

users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면? 

```sqlite
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

users에서 나이순, 성순으로 오름차순 정렬하여 상위 10개만 뽑아보면?

```sqlite
sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```

users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람 이름 10개만 뽑아보면?

```sqlite
sqlite> SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
```



## sql project

##### sql파일에 텍스트 형식으로 명령어 작성

```sqlite
CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
.mode csv
.import boxoffice.csv movies
.headers on
.mode column
SELECT * FROM movies;

```

##### 터미널에서 만들고 싶은 이름으로 sqlite3파일 생성

`sqlite3 pjt.sqlite3`

##### sql파일을 불러와서 pjt에 적용시킨다.

`.read sql파일이름`

