from django.http import HttpResponse
from django.shortcuts import render

def webpage1(request):
    return render(request,'project.html')

def webpage2(request):
    return render(request,'index.html')