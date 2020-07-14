from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def Register(request):
    return render(request, 'register.html')
def Login(request):
    return render(request, 'login.html')
def User_view(request):
    return render(request, 'user_view.html')
def Admin_view(request):
    return render(request, 'admin_view.html')
def Guest_view(request):
    return render(request, 'guest_view.html')

def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})