from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


def loginfunc(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def registerfunc(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)  # auto login after register
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def logoutfunc(request):
    logout(request)
    return redirect("login")
