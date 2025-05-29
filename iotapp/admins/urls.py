from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('admins_home/', views.admin_dashboard, name='admins_home'),

]
