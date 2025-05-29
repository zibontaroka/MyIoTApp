from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts_us/', views.contacts_us, name='contacts_form'),
    path('services/', views.services, name='services'),
    path('base/', views.base, name='base'),
    #path('about/', views.about, name='about'),
]
