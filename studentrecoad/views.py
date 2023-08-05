from django.shortcuts import render
from django.http import HttpResponse
import datetime
from.froms import  stufrom
# Create your views here.

def home(request):
    return HttpResponse('<h1>This is student list</h1>')

def date1(request):
    d=datetime.datetime.now()
    return HttpResponse(d)


def index(request):
    a=[
        {'name':'dhruvil','age':20,'email':'dhruvil201@gmail.com'},
        {'name':'guddi','age':20,'email':'guddi101@gmail.com'},
        {'name':'krish','age':22,'email':'krish221@gmail.com'},
        {'name':'aryan','age': 80,'email':'aryan299@gmail.com'},
        {'name':'rakshita','age': 28,'email':'rakshita22@gmail.com'},

       ]
    return render(request,'index.html',{'a1':a})

def create(request):
    f=stufrom()
    return render(request,'index.html',{'from':f})