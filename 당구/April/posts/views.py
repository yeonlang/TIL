from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})

def create(request):
    # Q2-2, Q2-3 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    pass

def like(request, post_id):
    # Q3-3 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    pass