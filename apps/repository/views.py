from django.shortcuts import render
from django.urls import reverse_lazy

from repository.models import Software
from repository.models import Category
from authentication.models import CustomUser

from repository.forms import SoftwareNewForm
from repository.forms import CategoryForm

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

# Create your views here.
class CategoryCreateView(CreateView):
    model = Category
    template_name = "repository/category/new.html"
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard')

class SoftwareCreateView(CreateView):
    model = Software
    template_name = "repository/new.html"
    form_class = SoftwareNewForm
    success_url = reverse_lazy('dashboard')


class SoftwareDetailView(DetailView):
    template_name = "repository/detail.html"
    model = Software

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context
    
    
    
    
    

