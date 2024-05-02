from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from repository.models import Software
from repository.models import Category
from authentication.models import CustomUser

from repository.forms import (
    SoftwareNewForm, SoftwareVersionForm,SoftwareOriginForm,
    CategoryForm,
    DescriptionForm,
)

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# View para ingresar la informacion sobre la licencia de software
class CategoryLicenseUpdateView(UpdateView):
    model = Category
    template_name = "repository/category_license.html"
    fields = ['software','license']
        
    def get_success_url(self):
        print(self.object)
        return reverse_lazy('category_general', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context

#view para ingresar la informacion de la categorizacion del software
class CategoryGeneralUpdateView(UpdateView):
    model = Category
    template_name = "repository/category.html"
    form_class = CategoryForm
    
    def get_success_url(self):
        print(self.object)
        return reverse_lazy('repository', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])

        return context
#
class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Software
    template_name = "repository/category_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context
    
#
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

#View para visualizar la informacion del software   
class SoftwareDetailView(DetailView):
    template_name = "repository/detail.html"
    model = Software

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context['repositories'] = Software.objects.filter(user=self.request.user)
        return context

#
class DescriptionUpdateView(UpdateView):
    model = Software
    template_name = "repository/description.html"
    form_class = DescriptionForm
    success_url = reverse_lazy('dashboard')
    
    def get_queryset(self):
        return super().get_queryset()
    
#View para ingresar la informacion de la version, tipo de obra(inedita o derivada) y fecha de creacion del software 
class SoftwareUpdateView(UpdateView):
    model = Software
    template_name = "repository/version.html"
    form_class = SoftwareVersionForm
    
    def get_success_url(self):
        return reverse_lazy('type_work', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context
    
#view para ingresar la informacion de la originalidad de la obra
class SoftwareOriginUpdateView(UpdateView):
    model = Software
    template_name = "repository/origin.html"
    form_class = SoftwareOriginForm
    
    def get_success_url(self):
        return reverse_lazy('category_license', kwargs={'slug': self.object.slug })

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        form = SoftwareOriginForm(self.request.POST)
        print(form)
        print(self.request.POST)
        return context
    

