from django.shortcuts import render
from django.http import HttpResponse
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
