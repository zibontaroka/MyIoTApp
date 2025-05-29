from django.shortcuts import render # type: ignore

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/base_dashboard.html')

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def profile_view(request):
    return render(request, 'base/base_nidex.html')

def edit_profile_view(request):

    return render(request, 'users/edit_profile.html')

def settings_view(request):
    return render(request, 'users/settings.html')