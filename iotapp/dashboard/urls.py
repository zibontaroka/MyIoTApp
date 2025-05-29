from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]