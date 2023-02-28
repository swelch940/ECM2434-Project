from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def map(reuqest):
    return HttpResponse("This will be the map page")

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