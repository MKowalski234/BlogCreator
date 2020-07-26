from django.urls import path
from . import views

#  czym różni się użycie path('') od url(r'^$') w urlpatterns?


# app_name = 'Blogowanie'
urlpatterns = [
    path('Blogs', views.list_of_blogs, name='Blogs'),
]