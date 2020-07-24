from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, User, Blog, Comment
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, UserForm, CommentForm, PostForm

# def Blogs(request):
#     all_blogs = Blog.objects.all()
#     return render(request, )

def Register(request):
    return render(request, 'register.html')

def Login(request):
    return render(request, 'login.html')

def Main_view(request):
    if request.user.is_authenticated(User):
        return render(request, 'user_view.html')
    else:
        return render(request, 'guest_view.html')

def Admin_view(request):
    return render(request, 'admin_view.html')



def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})