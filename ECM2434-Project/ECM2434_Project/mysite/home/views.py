#@authors Steven Welch, Joshua Curry, Callum Wilton, Nahum Hillier, Luis Hidalgo
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import RegisterForm
import json
from django.http import JsonResponse
from django.http import *
from django.utils import timezone
import math
import sys
from .bark_buddy import BarkBuddy
from json import dumps
from .models import Tree
#from .models import getLeaderboard

#Returns the home html page
def home(request):
    return render(request, 'home.html')

#Returns the map html page. Also returns the current coordinates via the url if the "Get current Location"
#button is pressed. 
def map(request):
    
    urlString = str(request)
    splitUrl = urlString.split("%3A=")
    if(len(splitUrl) == 2):
        #cords contains the longitude and latitude of the users current location
        #[0] is lat, [1]is lon
        cords = splitUrl[1].split("%2C")
        cords[1] = cords[1][:-1]
        cords[1] = cords[1][:-1]
    
    return render(request, 'map.html')


#Returns the leaderboard html page
def leaderboard(request):
    """ code for leaderboard """
    
    urlString = str(request)
    if('Sort=Plastic' in urlString):
        data = Tree.objects.all().order_by('-plastic_saved').values()
    else:
        data = Tree.objects.all().order_by('-oxygen').values()

    context = {
    'mymembers': data,
    }
    print(data)
    print(" ")

    print(context)

    return render(request, 'leaderboard.html', context)
    
#Returns the delete account html page. Also checks the URL string. If the
#url string contains "deleted=yes", i.e. the user has pressed the button
#to delete their account, then their account gets deleted 
def deleteaccount(request):
    """ Code for deleting account page """

    urlString = str(request)
    if('Deleted=yes' in urlString):
        member = Tree.objects.get(username = request.user)
        member.delete()
        goneUser = User.objects.get(username = request.user)
        goneUser.delete()

    return render(request, 'deleteaccount.html')

#Returns the new email html page. Also checks the URL string. If the
#url string contains "changedEmail", i.e. the user has changed their email
#on the webpage, then the email for their account gets changed. 
def newemail(request):
    """ Code for changing email """
    urlString = str(request)

    #If the email has been changed
    if('changedEmail=' in urlString):

        u =  u = User.objects.get(username = request.user)
        splitUrl = urlString.split("changedEmail=")
        newemailRaw = splitUrl[1]
        newemail = newemailRaw.replace('%40', '@')
        newemail = newemail[:-1]
        newemail = newemail[:-1]

        u.email = newemail
        u.save()

    return render(request, 'newemail.html')

#Returns the newpassword html page
def newpassword(request):
    """ Code for chaning users password """
    
    urlString = str(request)
    if('changedPassword=' in urlString):
        print("chaning password")

        u =  u = User.objects.get(username = request.user)
        splitUrl = urlString.split("changedPassword=")
        print(splitUrl)
        newpass = splitUrl[1]
        newpass = newpass[:-1]
        newpass = newpass[:-1]

        print(newpass)

        u.set_password(newpass)
        u.save()

    return render(request, 'newpassword.html')

#Returns the bottlesize html page
def bottlesize(request):
    """ Lets users change the size of water bottles """

    urlString = str(request)
    if('plasticAmount=' in urlString):
        print("changning amount in plastic bottle")
        t = Tree.objects.get(username = request.user)
        splitUrl = urlString.split('plasticAmount=')
        print(splitUrl)
        newbot = splitUrl[1]
        newbot = newbot[:-1]
        newbot = newbot[:-1]

        print(newbot)

        t.bottle_plastic = newbot
        t.save()

    return render(request, 'bottlesize.html')

#Returns the about html page  
def about(request):
    return render(request, 'about.html')

#Returns the settings html page
def settings(request):
    """ Code for sending values to and from back end """
    return render(request, 'settings.html')

#Returns the register html page. Also automatically saves any previously typed in 
#user credentials. 
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


#Returns the tree html page, alongside the current water level, oxygen level,
#plastic saved, and user level. 
def tree(request):
    
    #If the current user doesn't have a tree, then we generate a new tree
    if Tree.objects.filter(username=request.user).count() == 0:
        user = Tree.objects.create(username=request.user)
    
    #Else, if the user has a tree
    else:
        #Gets the tree object
        user = Tree.objects.get(username=request.user)

        #If the water level of the tree is zero, and it isn't in the tree house
        if user.water == 0 and user.in_greenhouse == False:
            #If the tree is alive
            if user.isAlive == True:
                #Kill the tree
                user.isAlive = False
                user.save()
            
            else: #figure out if new tree can be planted
                current = timezone.now()
                elapsed = current - user.last_active
                if elapsed.seconds >=86400:#if 24 hours since last tree planted
                    user = Tree.objects.create(username=request.user)

        #Else, if the tree is alive and in the greenhouse, the tree doesn't release any
        #oxygen, and the 
        elif user.in_greenhouse == False:#if not in greenhouse then tree updates
            current = timezone.now()
            elapsed = current - user.last_active
            count = elapsed.seconds // 7200
            if user.water < 20 or user.water > 80:
                w = (0.65*user.bottle_plastic)//5
            else:
                w = user.bottle_plastic//2
            user.oxygen += user.level*w*count*27 #updated oxygen
            if user.oxygen // (user.level)**7 > 0 and user.level < 100: #level up if possible
                user.level += 1
            user.water -= 1*count
            user.last_active = current
            user.plastic_saved += count * 8
            user.save()
    


    #Gets the current coordinates if the "Get current location" button is pressed. 
    urlString = str(request)
    #splitUrl = urlString.split("%3A=")
    if('cords%3A=' in urlString):
        #Cords contains the longitude and latitude of the users current location
        #[0] is the latitutde, [1]is longitude
        splitUrl = urlString.split("%3A=")
        cords = splitUrl[1].split("%2C")
        cords[1] = cords[1][:-1]
        cords[1] = cords[1][:-1]

        #If the current location is near a water fountain, then update the water meter, and
        #plastic saved
        if checkNearFountain(cords):
            user.water += 20
            user.plastic_saved += 10
            user.save()
    
    #Code for the green house
    if('Greenhouse=Clicked' in urlString):
        print("entering green house")

        t = Tree.objects.get(username=request.user)
        t.in_greenhouse = True
        t.save()
    
    if('Greenhouse=NotClicked' in urlString):
        print("Leaving Green house")

        t = Tree.objects.get(username=request.user)
        t.in_greenhouse = False
        t.save()


    oxygen = {"Oxygen":user.oxygen, "Water": user.water, "Plastic":user.plastic_saved,"Level":user.level}
    oxygen = dumps(oxygen)
    return render(request, 'tree.html', {"oxygen":oxygen})


#Checks whether or not the location of the user is "near" a water fountain. Returns true or false depending on if its
#near enough. 
def checkNearFountain(userCords):
    #Displacement is the pythagorean distance between the user and target
    displacement = math.sqrt((50.7390871 - float(userCords[0]))**2.0  + (-3.5382999 - float(userCords[1]))**2.0 )

    #0.0638 is just a place holder value. There's nothing significant about it. 
    if(displacement <= 0.0638):
        return True
    else:
        return False

