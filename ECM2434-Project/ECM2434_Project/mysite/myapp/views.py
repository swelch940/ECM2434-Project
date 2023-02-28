from django.shortcuts import render, redirect
from mysite.forms import RegisterForm


# Create your views here.


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