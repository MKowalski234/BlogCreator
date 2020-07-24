from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Post(forms.form):
    Poster_username=forms.CharField(label='username',max_length=50)
    Date_posted=forms.DateTimeField(label='posted')
    Post=forms.CharField(label='content',max_length=500)
