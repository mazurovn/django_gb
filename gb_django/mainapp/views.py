#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world (request):
    return HttpResponse("Hello world!!!")
def blog(request):
    return  HttpResponse('Helo blog')