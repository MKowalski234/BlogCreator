from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Blogowanie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blogowanie.urls', )),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('register/', views.register, name='register'),
    # path('',views.Main_view,name='main'),
    # path('administrate/',views.Admin_view,name='main'),
]
