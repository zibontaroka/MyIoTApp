from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('users_home/', views.users_dashboard, name='users_home'),

]
