from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import FormView

from authentication.models import CustomUser, Profile

from authentication.forms import RegisterUserForm, UserProfileForm

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

class CustomUserCreateView(TemplateView):
    model = CustomUser
    template_name = "authentication/signup.html"
    # success_url = reverse_lazy('perfil')
    
    def post(self, request):
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
              form.save()
              return redirect('profile_new', slug=request.POST.get('username'))
        else:
            form = RegisterUserForm()
        return redirect('signup')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterUserForm
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profile/edit.html"
    fields = '__all__'
    success_url = reverse_lazy('login')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile/detail.html"

class UserProfileView(UpdateView):
    model = Profile
    template_name = "profile/new.html"
    fields = ['occupation','institution','profession_career','avatar','gender']
    success_url = reverse_lazy('login')
    
def user_logout_view(request):
    logout(request)
    return redirect('index')
