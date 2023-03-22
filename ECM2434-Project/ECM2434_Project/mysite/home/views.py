#@authors Steven Welch, Joshua Curry, Callum Wilton, Nahum Hillier, Luis Hidalgo
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from mysite.forms import RegisterForm
from django.http import *
from django.utils import timezone
import math
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
        print("deleting account")
        
        member = Tree.objects.get(username = request.user)
        member.delete()
        goneUser = User.objects.get(username = request.user)
        goneUser.delete()

    return render(request, 'deleteaccount.html')
    
def newemail(request):
    """ Code for changing email """
    urlString = str(request)
    if('changedEmail=' in urlString):
        print("chaning email")

        u =  u = User.objects.get(username = request.user)
        splitUrl = urlString.split("changedEmail=")
        print(splitUrl)
        newemailRaw = splitUrl[1]
        newemail = newemailRaw.replace('%40', '@')
        newemail = newemail[:-1]
        newemail = newemail[:-1]
        print(newemail)

        u.email = newemail
        u.save()

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
    if Tree.objects.filter(username=request.user).count() == 0:#new tree
        user = Tree.objects.create(username=request.user)
        
    else:#existing trees
        user = Tree.objects.get(username=request.user)#get the tree object
        if user.water == 0 and user.in_greenhouse == False:#if water is zero then tree dies
            if user.isAlive == True:
                user.isAlive = False
                user.save()
            else: #figure out if new tree can be planted
                current = timezone.now()
                elapsed = current - user.last_active
                if elapsed.seconds >=86400:#if 24 hours since last tree planted
                    user = Tree.objects.create(username=request.user)

        elif user.in_greenhouse == False:#if not in greenhouse then tree updates
            current = timezone.now()
            elapsed = current - user.last_active
            count = elapsed.seconds // 7200#number of bihourly periods since last login
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
            user.save()#update object
    

    urlString = str(request)
    splitUrl = urlString.split("%3A=")
    if(len(splitUrl) == 2):
        #cords contains the longitude and latitude of the users current location
        #[0] is lat, [1]is lon
        cords = splitUrl[1].split("%2C")
        cords[1] = cords[1][:-1]
        cords[1] = cords[1][:-1]
        print(cords)

        if checkNearFountain(cords):#increases oxygen and plastic saved if near fountain
            user.water += 20
            user.plastic_saved += 10
            user.save()
            
            print("Near")

    oxygen = {"Oxygen":user.oxygen, "Water": user.water, "Plastic":user.plastic_saved,"Level":user.level}#values to pass to template
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
  data = Tree.objects.all
  list_username = {}
  for username in data:
      list_username[username]={"water": username["water"], "oxygen":username["oxygen"], "plastic":username["plastic_saved"]}

    
      
  return render(request, 'leaderboard.html', list_username)

