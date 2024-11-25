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

from home.models import App

from authentication.models import (
    Profile
)
from home.models import App

from authentication.forms import (
    RegisterUserForm,
    # UserProfileForm,
    # AcademicaForm, AcademicaRoleForm, AcademicaUniversityForm,
    ProfileContactForm,
    # CustomUserEditForm,
)

# Create your views here.

#view login
class UserLoginView(TemplateView):
    template_name = "authentication/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = App.objects.first()
        return context
    
    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user:
            login(request, user)
            if user.is_authenticated:
                messages.success(request, 'You have been logged in.')
                return redirect('dashboard')
        else:
            messages.success(request, 'There was Error logging in, Please try again.')
            return redirect('login')

#view register
class CustomUserCreateView(TemplateView):
    model = Profile
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
        context["app"] = App.objects.first()
        return context

# class ProfileView(CreateView):
#     model = Profile
#     template_name = "profile/edit.html"
#     form_class = UserProfileForm
#     success_url = reverse_lazy('login')

# class AcademicaCreateView(CreateView):
#     model = Academica
#     template_name = "profile/academica.html"
#     form_class = AcademicaForm
#     success_url = reverse_lazy('dashboard')
    
#     def form_valid(self, form):
#         res = form.save(commit=False)
#         print(res)
#         res.user = self.request.user
#         res.save()
#         return redirect(self.success_url)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["app"] = App.objects.first()        
#         return context
    
    
#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         print(response)
#         print(form.is_valid())
#         return redirect('dashboard')
    

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

# class CustomUserUpdateView(UpdateView):
#     model = CustomUser
#     template_name = "profile/edit.html"
#     form_class = CustomUserEditForm
#     success_url = reverse_lazy('profile')

# # define el rol(estudiante o profesor)  
# class AcademicaRoleView(LoginRequiredMixin, TemplateView):
#     template_name = "profile/role.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         context["form"] = AcademicaRoleForm
#         context["app"] = App.objects.first()
#         return context
    
#     def post(self, request):
#         if request.method == 'POST':
#             form = AcademicaRoleForm
#             form.user = request.POST.get('user')
#             form.rol = request.POST.get('rol')

#             if form.is_valid:
#                 academica_obj = Academica.objects.get(user_id=request.user.id)
#                 academica_obj.rol = request.POST.get('rol')
#                 academica_obj.save()
#                 return redirect('university')
#             else:
#                 return redirect('role')

# # define la institucion de pertenecia del usuario
# class AcademicaUniveristyView(TemplateView):
#     template_name = "profile/university.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = AcademicaUniversityForm
#         context["app"] = App.objects.first()
#         return context
    
#     def post(self, request):
#         if request.method == 'POST':
#             academica_obj = Academica.objects.get(user_id=request.user.id)

#             if academica_obj:
#                 academica_obj.university = request.POST.get('university')
#                 academica_obj.profession = request.POST.get('profession')

#                 if academica_obj.rol == 'ESTUDIANTE':
#                     academica_obj.semester = request.POST.get('semester')
#                 academica_obj.save()
                
#                 return redirect('dashboard')
#             else:
#                 return redirect('university')
 
def user_logout_view(request):
    logout(request)
    return redirect('index')

