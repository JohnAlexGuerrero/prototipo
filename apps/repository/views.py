from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from repository.models import Software
from repository.models import Category
from repository.models import Requeriment
from repository.models import Author
from repository.models import Installation
from authentication.models import Profile as CustomUser

from repository.forms import (
    SoftwareCreateForm, SoftwareVersionForm,SoftwareOriginForm,
    CategoryForm,
    DescriptionForm, RequerimentForm,
    SoftwarePublicForm, AuthorsForm
)
from home.models import App, Template

from django.views.generic import CreateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import View, ListView

import os
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse

#view utilizado para la creacion de un nuevo registro
class SoftwareCreateView(LoginRequiredMixin, CreateView):
    model = Software
    template_name = "repository/new.html"
    form_class = SoftwareCreateForm
    
    def get_success_url(self):
        print(self.object)
        return reverse_lazy('logo', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SoftwareCreateForm
        context["app"] = App.objects.first()
        return context


#view para definir y/o actualizar el logo del software
class SoftwareLogoView(UpdateView):
    model = Software
    fields = ("logo",)
    template_name = "repository/logo.html"
    
    def get_success_url(self):
        return reverse_lazy('version', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        print(self.request.POST)
        return context

#View para ingresar la informacion de la version, pais de creacion y fecha de creacion del software 
class SoftwareVersionView(UpdateView):
    model = Software
    template_name = "repository/version.html"
    form_class = SoftwareVersionForm
    
    def get_success_url(self):
        return reverse_lazy('type_work', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
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
        context["app"] = App.objects.first()
        return context

# View para ingresar la informacion sobre la licencia de software
class CategoryLicenseUpdateView(UpdateView):
    model = Category
    template_name = "repository/category_license.html"
    fields = ['software','license']
        
    def get_success_url(self):
        print(self.object)
        return reverse_lazy('public', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context
    
    
#view para definir tipo de publico
class SoftwarePublicView(UpdateView):
    model = Software
    template_name = "repository/public.html"
    form_class = SoftwarePublicForm
    
    def get_success_url(self):
        return reverse_lazy('platform', kwargs={'slug': self.object.slug })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context
    
#view installation and configuration new
class PlatformView(CreateView):
    model = Installation
    fields = ['software', 'platform']
    template_name = "repository/platform.html"
    
    def get_queryset(self):
        return Installation.objects.get(software__slug=self.kwargs['slug'])
  
    def get_success_url(self):
        return reverse_lazy('hardware', kwargs={'slug': self.object.software.slug, 'pk': self.object.id })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        print(self.request.POST)
        return context

class InstallationUpdateView(UpdateView):
    model = Installation
    template_name = "repository/hardware.html"
    fields = ['software','os','procesador','storage','ram','screen']
    
    def get_success_url(self):
        return reverse_lazy('authors', kwargs={'slug': self.object.software.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context

#view registro de autor(es)
class AuthorView(CreateView):
    model = Author
    template_name = "repository/author.html"
    form_class = AuthorsForm
    
    def get_success_url(self):
        return reverse_lazy('detail_author', kwargs={'slug': self.object.software.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        print(self.request.POST)
        return context

#view para visualizar los autores
class AuthorListView(ListView):
    model = Author
    template_name = "repository/authors.html"
    
    def get_queryset(self):
        return Author.objects.filter(software__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context

def delete_author(request, *args, **kwargs):
    author = Author.objects.filter(software__slug=kwargs['slug']).filter(id=kwargs['pk'])
    # print(author)
    print(kwargs['slug'])
    print(kwargs['pk'])
    author.delete()
    return reverse_lazy('detail_author', kwargs={'slug':request.GET.get('slug')})

    
def generate_user_manual(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    
    return None


#view generar manual de usuario
class UserManualView(View):
    def get(self, request, *args, **kwargs):
        software = Software.objects.get(slug=self.kwargs['slug'])
        data = {
            'software': software
        }
        
        pdf = generate_user_manual('repository/user-manual.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    
    


#view para ingresar la informacion de la categorizacion del software
class CategoryGeneralUpdateView(UpdateView):
    model = Category
    template_name = "repository/category.html"
    form_class = CategoryForm
    
    def get_success_url(self):
        return reverse_lazy('repository', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context
#
class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Software
    template_name = "repository/category_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context
    

#View para visualizar la informacion del software   
class SoftwareDetailView(DetailView):
    template_name = "repository/detail.html"
    model = Software

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context['repositories'] = Software.objects.filter(user=self.request.user)
        context['app'] = App.objects.first()
        return context

#view para actualizar la caracterizacion del software
class DescriptionUpdateView(UpdateView):
    model = Software
    template_name = "repository/description.html"
    form_class = DescriptionForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('requeriment_new', kwargs={'slug':self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context['app'] = App.objects.first()
        return context
    

#view para agregar los requerimientos de un producto software
class SoftwareRequerimentsView(TemplateView):
    template_name = "repository/requeriments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requeriments'] = Requeriment.objects.filter(software__slug=self.kwargs['slug'])
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context


#view para agregar un requerimiento del sistema
class RequerimentNewView(CreateView):
    model = Requeriment
    form_class = RequerimentForm
    template_name = 'repository/requeriment_new.html'
    
    def get_success_url(self):
        return reverse_lazy('repository', kwargs={'slug': self.object.software.slug })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        return context

#view actualizar requeriment
class RequerimentUpdateView(UpdateView):
    model = Requeriment
    fields = ("software","name","description","version","image")
    template_name = "repository/requeriment_new.html"

    def get_success_url(self):
        return reverse_lazy('repository', kwargs={'slug': self.object.software.slug })
    
    def get_object(self, **kwargs):
        software_slug = self.kwargs['software_slug']
        requirement_slug = self.kwargs['requirement_slug']

        software = Software.objects.get(slug=software_slug)
        requirement = Requeriment.objects.get(slug=requirement_slug)

        return requirement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['software_slug'])
        context['templates'] = Template.objects.all()
        return context


#Eliminar un repositorio
class SoftwareDeleteView(DeleteView):
    model = Software
    fields = ("id",)
    template_name = "repository/delete.html"
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        return context


#view registe code source software
class CodeSourceView(TemplateView):
    template_name = "repository/code_source.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        print(self.request.POST)
        return context



#view solicitud de registro de proteccion de derechos de autor
class CopyrightView(TemplateView):
    template_name = "repository/request_copyright.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software"] = Software.objects.get(slug=self.kwargs['slug'])
        context["app"] = App.objects.first()
        print(self.request.POST)
        return context
