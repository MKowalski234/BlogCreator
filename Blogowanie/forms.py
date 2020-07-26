from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Comment, Post, Blog, User



class Post(forms.Form):
    Poster_username=forms.CharField(label='username',max_length=50)
    Date_posted=forms.DateTimeField(label='posted')
    Post=forms.CharField(label='content',max_length=500)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

