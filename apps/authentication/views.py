from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views.generic import TemplateView
from django.views.generic import CreateView

from authentication.models import CustomUser

from authentication.forms import RegisterUserForm

# Create your views here.
class UserLoginView(TemplateView):
    template_name = "authentication/login.html"

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('dashboard')
        else:
            messages.success(request, 'There was Error logging in, Please try again.')
            return redirect('login')

class CustomUserCreateView(CreateView):
    model = CustomUser
    template_name = "authentication/signup.html"
    form_class = RegisterUserForm
    
def user_logout_view(request):
    logout(request)
    return redirect('index')
