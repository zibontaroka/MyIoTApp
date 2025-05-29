
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
import home, dashboard, admins, users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls') ),
    path('', include('dashboard.urls') ),
    path('', include('admins.urls') ),
    path('', include('users.urls') ),
    
 
]