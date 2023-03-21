#@authors Steven Welch, Joshua Curry, Callum Wilson, Nahum Hillier, Luis Hidalgo
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import RegisterForm
import json
from django.http import JsonResponse
from django.http import *
import math
import sys
from . import bark_buddy
from json import dumps
from .models import Leaderboard
from .models import getLeaderboard

def home(request):
    return render(request, 'home.html')

def map(request):#map page
    
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
    return render(request, 'leaderboard.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context = {
        'form':form,
    }
    return render(request, 'register/register.html',context)


def tree(request):

    with open("text.txt", "r") as f:
        lines = f.readlines()
        spam = int(lines[0])
        eggs = int(lines[1])
        DB = bark_buddy.BarkBuddy(1, "user", water = spam, oxygen= eggs)

    oxygen = {"Oxygen":eggs, "Water": spam}
    
    urlString = str(request)
    splitUrl = urlString.split("%3A=")
    if(len(splitUrl) == 2):
        #cords contains the longitude and latitude of the users current location
        #[0] is lat, [1]is lon
        cords = splitUrl[1].split("%2C")
        cords[1] = cords[1][:-1]
        cords[1] = cords[1][:-1]
        print(cords)

        if checkNearFountain(cords):
            eggs +=1
            spam +=5
            with open("text.txt", "w") as f :
                f.write(str(spam) +"\n" +str(eggs))
            
    test = {"test":DB.oxygen}
    oxygen = dumps(oxygen)
    
    return render(request, 'tree.html', {"oxygen":oxygen})


def checkNearFountain(userCords):
    """checks if the user is near a fountain"""
    displacement = math.sqrt((50.7390871 - float(userCords[0]))**2.0  + (-3.5382999 - float(userCords[1]))**2.0 )#pythagorean distance between user and target
    print(displacement)
    if(displacement <= 0.0638): #place holder value to be adjusted(try 0.00638?)
        return True
    else:
        return False
    
def leaderboardView(request):
    leaderboardData = getLeaderboard()
    return render(request, 'leaderboard.html', {'leaderboardData': leaderboardData})