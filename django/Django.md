## Django  

## 1. 셋팅

##### 가상환경을 적용한 후에 장고를 설치한다.

```bash
$ pyenv virtualenv 3.6.7 {가상환경이름}-venv
$ pyenv local {가상환경이름}-venv
$ pip install django
```

##### django-admin startproject 프로젝트명

```bash
$ django-admin startproject {프로젝트명} .(.은 django admin과 같이 쓰인다.) 
# . 이 없다면 하위 디렉토리로 한번 더 접근하여 프로젝트를 시작한다.
$ python manage.py startapp {앱 이름}
```

##### 어플 폴더로 들어가서 templates 폴더를 생성해준다.

##### settings.py 를 설정한다.

```python
#실행했을때의 호스트 주소를 입력
ALLOWED_HOSTS=['playground-닉네임.c9users.io']

#서버를 실행시켜 준다.
python manage.py runserver $IP:$PORT

#앱에 저장되어있는 클래스를 호출 이름 예시는 'student.apps.StudentConfig'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '어플이름.apps.어플이름(첫글자는 대문자)Config',
]

```



## 1-1 어플리케이션

##### views.py에 실행페이지를 함수형식으로 작성

```python
# Create your views here.
def info(request):
    return render(request, 'info.html' )
    
def detail(request, name):
    return render(request, 'detail.html', {'name':name})
```

##### urls.py에서 페이지 주소값을 받아오는 경로로 지정해준다.(경로 import 필요)

```python
# pages앱(폴더) 내부에 존재하는 views.py를 import
from pages import views 

urlpatterns = [
    path('detail/<str:name>', views.detail),
    path('info/', views.info),
    path('admin/', admin.site.urls),
]
```

##### templates 폴더에 html 파일을 생성해준다.

```html
<!--경로는 프로젝트폴더/앱폴더/templates/html이름 -->

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{name}} 입니다.</h1>
</body>
</html>
```

##### 서버를 실행한다.

```bash
$ python manage.py runserver $IP:$PORT
```





## 1-2 모델만들기

##### models.py에 DB생성을 위해 클래스를 생성해준다. 

```python
class 클래스이름(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    birthday=models.DateField()
    age=models.IntegerField()
    
    #__str__을 오버라이드 함으로써 admin페이지에서 이 클래스를 호출하였을 시에 이름을 보여주도록 하는 함수. 
    def __str__(self):
        return self.name   
```

##### admin.py에 클래스를 import

```python
from .models import Post

admin.site.register(Post)

# 아래와 같은 형태의 방식으로 admin페이지에서 보여주는 형식을 변경할 수도 있다.
# class PostAdmin(admin.ModelAdmin):
#    list_display = ('title','content',)

# admin.site.register(Post, PostAdmin)
```

##### 마이그레이션을 한다.

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

##### 어드민 계정을 생성해준다.

```bash
$ python manage.py createsuperuser
```

##### 서버를 실행한다.

```bash
$ python manage.py runserver $IP:$PORT
```



## url 설정

##### url에 이름을 지정해 줄 수 있다.

```python
app_name='posts'

urlpatterns = [
    path('', views.index, name='list'),
]
```

##### views.py 에서 불러오는 방법은 다음과 같다.

* ##### python

```python
#urls의 경로가 다음과 같을 때 path('', views.index, name='list'),
return redirect('posts:list')

# urls내부 path('<int:post_id>/', views.detail, name='detail'),
# 위와 같은 변수를 요구할때 
return redirect('posts:detail', post.pk)
```

* ##### html(진자 템플릿 이용)

```html
<!--urls의 경로가 다음과 같을 때 path('', views.index, name='list'),-->
<a href='{% url 'posts:new' %}'>new</a>

<!-- urls내부 path('<int:post_id>/', views.detail, name='detail'),-->
<!-- 위와 같은 변수를 요구할때-->
<a href='{% url "posts:detail" post.pk %}'>{{post.title}}</a>
```

