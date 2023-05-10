import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import *

username_validator = UnicodeUsernameValidator()


class RegisterUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": ("Пароли не схожи"),
    }
    username = forms.CharField(
        label=('Имя пользователя'),
        max_length=150,
        help_text=(''),
        validators=[username_validator],
        error_messages={'unique': ("Такой пользователь существует")},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label=('Пароль'), widget=(forms.PasswordInput(attrs={'class': 'form-control'})), help_text=''
    )
    password2 = forms.CharField(
        label=('Подтверждение пароля'),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=('Введите пароль повторно'),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите email"}),
    )
    first_name = forms.CharField(
        label="Имя",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите имя"}),
    )
    last_name = forms.CharField(
        label="Фамилия",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите фамилию"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
        labels = {
            "username": "Имя пользователя",
            "email": "Email",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class ticketForm(forms.ModelForm):
    time_origin = forms.TimeField(
        label="Время вылета",
        required=False,
        widget=DateInput(attrs={'type': 'time'}),
        initial=datetime.date.today(),
        localize=True,
    )
    time_dest = forms.TimeField(
        label="Время прилета",
        required=False,
        widget=DateInput(attrs={'type': 'time'}),
        initial=datetime.date.today(),
        localize=True,
    )
    date_origin = forms.DateField(
        label="Дата вылета",
        required=False,
        widget=DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today(),
        localize=True,
    )
    date_dest = forms.DateField(
        label="Дата прилета",
        required=False,
        widget=DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today(),
        localize=True,
    )

    class Meta:
        model = Tickets
        fields = '__all__'
        labels = {
            "name_origin": "Город вылета",
            "name_dest": "Город прилета",
            "name_origin_aero": "Аэропорт вылета",
            "name_dest_aero": "Аэропорт прибытия",
            "time_origin": "Время и дата вылета",
            "time_dest": "Время и дата прилета",
            "date_origin": "Время и дата прилета",
            "date_dest": "Время и дата прилета",
            "ticket_price": "Цена билета",
            "type_of_flight": "Тип класса",
        }
