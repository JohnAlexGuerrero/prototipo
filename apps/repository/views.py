from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from repository.models import Software
from repository.models import Category
from authentication.models import CustomUser

from repository.forms import (
    SoftwareNewForm,
    CategoryForm,
    DescriptionForm,
)

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Create your views here.
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "repository/category/new.html"
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard')

class SoftwareCreateView(LoginRequiredMixin, TemplateView):
    model = Software
    template_name = "repository/new.html"

    def post(self, request):
        if request.method == 'POST':
            form = SoftwareNewForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            return redirect('repository_new')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SoftwareNewForm
        return context
    
class SoftwareDetailView(DetailView):
    template_name = "repository/detail.html"
    model = Software

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context['repositories'] = Software.objects.filter(user=self.request.user)
        return context
    
class DescriptionUpdateView(UpdateView):
    model = Software
    template_name = "repository/description.html"
    form_class = DescriptionForm
    # success_url = reverse_lazy('repository', slug=get_object)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["repositories"] = Software.objects.filter(user=self.request.user)
        print(context)
        return context
    
    def get_object(self):
        print(self.request)
        return self.request.user

    def success_url(self, *args, **kwargs):
        res = redirect('dashboard')
        return res
    

    
    
    

