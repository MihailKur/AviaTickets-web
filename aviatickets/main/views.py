from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import *


def index(response):
    return render(response, 'main/index.html')

def aboutUs(response):
    return render(response, 'main/about.html')

def profile(response):
    user_info = User.objects.all()
    return render(response, 'main/cabinet.html',{'user_info':user_info})

@login_required(login_url="/")
def change_profile(request):
    user_info = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = RegisterUserForm(request.POST or None, instance=user_info)
        if form.is_valid():
            form.save()
            user_info.username = request.POST["username"]
            user_info.email = request.POST["email"]
            login(request, user_info)
            messages.success(request, "Данные успешно обновлены")
            return redirect("profile")
    else:
        form = RegisterUserForm(instance=user_info)
    context = {"form": form}
    return render(request, "main/change_profile.html", context)

def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы вошли как " + username)
            return redirect("home")
        else:
            messages.warning(request, "Логин или пароль неверны")
            return render(request, "main/login.html")
    else:
        return render(request, "main/login.html")
    

def registry(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы зарегистрировались как " + username))
            return redirect("home")
    else:
        form = RegisterUserForm()
    return render(request, "main/register.html", {"form": form})


@login_required(login_url='/')
def logoutuser(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта"))
    return redirect("home")