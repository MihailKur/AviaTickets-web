from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import *


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


def about_us(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/about.html')


def sales(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/sales.html')


def profile(request: HttpRequest) -> HttpResponse:
    user_info = User.objects.all()
    user_sales_count = UsersSales.objects.filter(user=request.user)
    return render(request, 'main/cabinet.html', {'user_info': user_info, "user_sales_count": user_sales_count})


@login_required(login_url="/")
def change_profile(request: HttpRequest) -> HttpResponse:
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


def loginuser(request: HttpRequest) -> HttpResponse:
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


def registry(request: HttpRequest) -> HttpResponse:
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
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта"))
    return redirect("home")


@staff_member_required
def create_ticket(request: HttpRequest) -> HttpResponse:
    submitted = False
    if request.method == "POST":
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/create?submitted=True")
    else:
        form = ticketForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "main/create.html", {"form": form, "submitted": submitted})


def search_ticket(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        error = None
        name_origin = request.GET.get("origin")
        name_dest = request.GET.get("dest")
        date_origin = request.GET.get("date_travel")
        if not date_origin:
            tickets = Tickets.objects.filter(name_origin=name_origin, name_dest=name_dest)
        else:
            tickets = Tickets.objects.filter(name_origin=name_origin, name_dest=name_dest, date_origin=date_origin)
        if not tickets:
            error = "Билетов на данную дату нет!"
        return render(request, "main/search.html", {"tickets": tickets, "error": error})
    if request.method == "POST":
        user_id = request.POST["user_id"]
        ticket_id = request.POST["ticket_id"]
        sale = UsersSales.objects.create(user_id=user_id, ticket_id=ticket_id)
        sale.save()
        messages.success(
            request, ("Ваша бронь успешно оформлена! В скором времени наша служба с вами свяжется для оплаты.")
        )
        return redirect("home")


def search_sales(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        userssale_id = request.POST["sale_id"]
        ticket_delete = UsersSales.objects.get(id=userssale_id)
        if ticket_delete.user == request.user:
            ticket_delete.delete()
            messages.success(request, ("Ваша бронь успешно отменена!"))
            return redirect("sales")
    user_sales = UsersSales.objects.filter(user=request.user)
    waste = None
    if not user_sales:
        waste = "У вас пока нет ни одной брони!"
    return render(request, "main/sales.html", {"user_sales": user_sales, "waste": waste, "user": request.user})
