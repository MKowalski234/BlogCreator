from django.contrib import admin
from django.urls import path, include

from Blogowanie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blogowanie.urls',)),
    # path('login/',views.Login,name='login'),
    # path('register/',views.Register,name='register'),
    # path('',views.Main_view,name='main'),
    # path('administrate/',views.Admin_view,name='main'),

]
