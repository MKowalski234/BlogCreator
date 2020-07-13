from django.shortcuts import render
from django.http import HttpResponse
def Register(request):
    return render(request, 'base.html')
def Login(request):
    return render(request, 'base.html')
def User_view(request):
    return render(request, 'base.html')
def Admin_view(request):
    return render(request, 'base.html')
def Guest_view(request):
    return render(request, 'base.html')
