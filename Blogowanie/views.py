from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

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
    comments = post.comments.filter(activate=True)

    if request.method =='POST':
        # publikowanie komentarza
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # tworzenie obiektu Comment bez zapisu w bazie danych
            new_comment = comment_form.save(commit=False)
            # przypisanie komentarza do bieżącego posta
            new_comment.post = post
            # zapisanie komentarza w bazie danych
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, 'blog/post/detail.html', {'post': post,
                                                         'comments': comments,
                                                         'comments_form': comment_form})
