from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Blogowanie'
urlpatterns = [
    path('', views.post_list, name='post_list'),
]