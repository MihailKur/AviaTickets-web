from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.aboutUs, name='aboutUs'),
    path('login/', views.loginuser, name='login'),
    path('registry/', views.registry, name='registry'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.change_profile, name='change_profile')
]
