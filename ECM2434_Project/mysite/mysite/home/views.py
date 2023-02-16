from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def map(reuqest):
    return HttpResponse("This will be the map page")

def leaderboard(request):
    return HttpResponse("This will be the leaderboard page")