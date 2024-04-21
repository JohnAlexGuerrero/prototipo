from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import FormView

from authentication.models import CustomUser, Profile, Academica

from authentication.forms import (
    RegisterUserForm,
    UserProfileForm,
    AcademicaForm,
    ProfileContactForm,
)

# Create your views here.
class UserLoginView(TemplateView):
    template_name = "authentication/login.html"

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user:
            login(request, user)
            if user.is_authenticated:
            #     return redirect("profile_new", slug=user.profile.slug)
            # else:
                messages.success(request, 'You have been logged in.')
                return redirect('dashboard')
        else:
            messages.success(request, 'There was Error logging in, Please try again.')
            return redirect('login')

class CustomUserCreateView(TemplateView):
    model = CustomUser
    template_name = "authentication/signup.html"
    
    def post(self, request):
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
              form.save()
              #Authentication and login
              email = form.cleaned_data['email']
              password = form.cleaned_data['password1']
              user = authenticate(email=email, password=password)
              login(request, user)
              messages.success(request, 'You have successfull.')

              if user.is_authenticated:
                # return redirect("profile_new", slug=user.profile.slug)
                return redirect('login')
        else:
            form = RegisterUserForm()
        return redirect('signup')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterUserForm
        return context

class ProfileView(CreateView):
    model = Profile
    template_name = "profile/edit.html"
    form_class = UserProfileForm
    success_url = reverse_lazy('login')

class AcademicaCreateView(CreateView):
    model = Academica
    template_name = "profile/academica.html"
    form_class = AcademicaForm
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        res = form.save(commit=False)
        print(res)
        res.user = self.request.user
        res.save()
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(response)
        print(form.is_valid())
        return redirect('dashboard')
    

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile/detail.html"

class UserProfileView(UpdateView):
    model = Profile
    template_name = "profile/new.html"
    fields = '__all__'
    success_url = reverse_lazy('login')

class ContactUpdateView(UpdateView):
    model = Profile
    template_name = "profile/contact.html"
    form_class = ProfileContactForm
    success_url = reverse_lazy('profile')
    
def user_logout_view(request):
    logout(request)
    return redirect('index')

