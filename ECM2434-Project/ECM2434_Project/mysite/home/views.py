from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import RegisterForm
import json
from django.http import JsonResponse
from django.http import *

def home(request):
    return render(request, 'home.html')

def map(request):

    print(request)
    
    urlString = str(request)
    splitUrl = urlString.split("%3A=")
    if(len(splitUrl) == 2):
        #cords contains the longitude and latitude of the users current location
        #[0] is lat, [1]is lon
        cords = splitUrl[1].split("%2C")
        cords[1] = cords[1][:-1]
        cords[1] = cords[1][:-1]
    
    return render(request, 'map.html')

def leaderboard(request):
    return HttpResponse("This will be the leaderboard page")


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        'form':form,
    }
    return render(request, 'register/register.html',context)


def tree(request):
    return render(request, 'tree.html')