from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello from my Django app</h1>")

def thing1(request):
    return HttpResponse("Hello from the first thing")

def thing2(request):
    return HttpResponse("Hello from the second thing")
