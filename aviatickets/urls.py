from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_us, name='about'),
    path('login/', views.loginuser, name='login'),
    path('registry/', views.registry, name='registry'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('sales/', views.sales, name='sales'),
    path('create', views.create_ticket, name="create"),
    path('search', views.search_ticket, name="search"),
    path('sales', views.search_sales, name="sales"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
