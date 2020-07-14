from django.contrib import admin
from django.urls import path, include

from Blogowanie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Guest_view,name='main'),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('logged',views.User_view,name='main'),
    path('administrate/',views.Admin_view,name='main'), # todo pojawia się pytanie, trzeba zrobić algorytm sprawdzający kim jest użytkownik aby pokazywało odpowiedni view
    path('Blogowanie/', include('Blogowanie.urls', namespace='blog')),
]
