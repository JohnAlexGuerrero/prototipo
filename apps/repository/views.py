from django.shortcuts import render
from django.urls import reverse_lazy

from repository.models import Software

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

# Create your views here.
class SoftwareCreateView(CreateView):
    model = Software
    template_name = "repository/new.html"
    fields = ['user','title','description','version','license']
    success_url = reverse_lazy('dashboard')

class SoftwareDetailView(DetailView):
    template_name = "repository/detail.html"
    
    

