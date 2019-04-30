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
# 프로젝트 이름과 앱 이름은 달라야 한다.
```

##### 어플 폴더로 들어가서 templates 폴더를 생성해준다.

##### settings.py 를 설정한다.

```python
#실행했을때의 호스트 주소를 입력
ALLOWED_HOSTS=['최상위폴더이름(ex:playground)-닉네임.c9users.io']

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



## 1:N구조

##### 정의 : `게시글과 댓글처럼 하나의 주격에 여러가지 보조격이 달라붙는 형태`

##### models.py 에 다음과 같은 청사진을 구성해 본다.

```python
# Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

#ForeignKey항목은 보조격에 붙어있어야 한다. 

# on_delete 옵션
# 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.(ex: 게시글이 삭제되면 댓글도 삭제)
# 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
# 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL로 변경
    
```

##### python shell에서 다음과 같이 확인해보자

```PYTHON
#python manage.py shell
from posts.models import Post, Comment

post = Post(title='제목입니다.', content='내용입니다.')
post.save()
Post.objects.all()

<QuerySet [<Post: Post object (1)>, <Post: Post object (7)>, <Post: Post object (8)>, <Post: Post object (9)>, <Post: Post object (10)>, <Post: Post object (11)>, <Post: Post object (17)>, <Post: Post object (18)>]>

post = Post.objects.last()
post
<Post: Post object (18)>

c = Comment(post=post, content='댓글입니다!')                           c.save()

#코멘트로 접근하여 모든 항목 불러오기
Comment.objects.all()
<QuerySet [<Comment: Comment object (1)>]>

#포스트로 접근하여 모든 항목 불러오기
post.comment_set.all()
<QuerySet [<Comment: Comment object (1)>]>

# 어떤 코멘트만 가져와서 살펴볼 수도 있다.
c = Comment.objects.get(pk=1)
c.post
<Post: Post object (18)>
    
    
post.comment_set.first()
<Comment: Comment object (1)>

post.comment_set.first().content
'댓글입니다!'

```



## 이미지 업로드

##### pip install

```bash
pip install Pillow
pip install pilkit
pip install django-imagekit
```

##### migration-models.py

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# 클래스에 아래와 같은 이미지 속성을 지정해준다.
class Post(models.Model):
    image = ProcessedImageField(
            upload_to='posts/images', # 저장 위치
            processors=[ResizeToFill(300,300)], # 처리할 작업 목록
            # ResizeToFill : 300,300 맞추고 넘치는 부분 잘라냄
			# ResizeToFit : 300,300 맞추고 남는 부분을 빈 공간으로 둠
        	format='JPEG', #저장 포맷 (확장자)
            options={'quality':90}, #저장 포맷 관련 옵션
        )
```

##### 이미지 저장경로 설정

```python
from django.conf.urls.static import static
from django.conf import settings

#여러 경로를 추가해줘야하기때문에 기존 경로 아래에 다음과 같은 코드를 작성한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

##### settings.py

```python
INSTALLED_APPS = [
    'imagekit',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'crud', 'assets'),   
]
#base 프로젝트 폴더 내부, crud/assets 를 기본 폴더로 한다. 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

##### views.py

```python
#이미지는 파일 형식이기 때문에 FILES로 받아온다.
def create(request):    
    image = request.FILES.get('image')
```

##### html

```python
#진자 탬플릿을 사용하여 현재 레벨에 있는 static 폴더 내부의 tree.jpg
<img src="{% static 'tree.jpg' %}">
#settings에 설정된 경로를 이용
<img src="{{ post.image.url }}"></img>
```



## BASE.HTML 설정

##### 프로젝트 내부에 templates 폴더 생성후 내부에 base.html 만들기

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    {% block container %}
    
    
    
  
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
</body>
</html>
```

##### settings.py에 경로를 추가한다.

```python
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR,'web','templates')],
    },
]
```

##### 앱 내부 templates/html에 적용한다.

```html
{% extends 'base.html' %}
<!--이미지 파일과 같은 static 적용시 필요-->
{% load static %}
{% block container %}

{% endblock %}
```



### 설치프로그램

```python
django==2.1.8
djangorestframework
django-rest-swagger
```



