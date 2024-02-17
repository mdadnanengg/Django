from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home (req):
    return render(req, 'home.html', {'name': 'Adnan'})

def add(req):
    val1 = int(req.POST['num1'])
    val2 = int(req.POST['num2'])
    res = val1 + val2

    return render(req, 'result.html', {'result': res})
