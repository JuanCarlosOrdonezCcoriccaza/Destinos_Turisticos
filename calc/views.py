from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render( request ,'home.html',{'name':'Juan'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    resultado = val1 + val2 
    return render(request ,"result.html",{'resultado':resultado})