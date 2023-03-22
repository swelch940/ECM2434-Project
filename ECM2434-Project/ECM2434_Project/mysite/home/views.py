#@authors Steven Welch, Joshua Curry, Callum Wilton, Nahum Hillier, Luis Hidalgo
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
from .bark_buddy import BarkBuddy
from json import dumps
from .models import Tree
#from .models import getLeaderboard

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
    
def deleteaccount(request):
    """ Code for deleting account page """

    urlString = str(request)
    if('Deleted=yes' in urlString):
        print("Here")
        
        member = Tree.objects.get(username = request.user)
        member.delete()
        goneUser = User.objects.get(username = request.user)
        goneUser.delete()

    return render(request, 'deleteaccount.html')
    
def newemail(request):

    return render(request, 'newemail.html')
    
def newpassword(request):
    return render(request, 'newpassword.html')
    
def bottlesize(request):
    return render(request, 'bottlesize.html')

def about(request):
    return render(request, 'about.html')

def settings(request):
    """ Code for sending values to and from back end """

    print("We at settings page")

    return render(request, 'settings.html')

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

    
    #Getting/Creating the users tree
    if Tree.objects.filter(username = request.user):
        userStats = Tree.objects.filter(username = request.user).values()
        for value in userStats:
            bb = BarkBuddy(1, value["username"],value["oxygen"], value["water"], plastic = value["plastic_saved"] )
            print(userStats)
    else:
        bb = BarkBuddy(1, request.user)
    
    #Saving values to the tree
    bbTree = Tree(request.user, bb.oxygen, bb.level, bb.plastic, True, bb.endurance, bb.water)
    bbTree.save()
    
    

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
            user = Tree.objects.get(username = request.user)
            user.oxygen += 1
            user.water += 5
            user.plastic_saved += 10
            user.save()
            
            print("Near")

    oxygen = {"Oxygen":bb.oxygen, "Water": bb.water, "Plastic":bb.plastic}
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


#def leaderboardView(request):
 #   leaderboardData = getLeaderboard()
 #   return render(request, 'leaderboard.html', {'leaderboardData': leaderboardData})