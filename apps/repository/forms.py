from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from django import forms
from django.forms import MultipleChoiceField

from repository.models import Software, Requeriment
from repository.models import Category, Task, Author
from authentication.models import Profile

#formulario para la creacion de un nuevo registro 
class SoftwareCreateForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['user','title']
        
        widgets = {
            "title": forms.TextInput(attrs={
                'class':'form-control form-control-sm shadow p-3',
            })
        }


#form de category
class CategoryForm(forms.ModelForm):
    tasks =  forms.MultipleChoiceField(label='Actividades', choices=Task.choices, widget=forms.SelectMultiple(attrs={'class': 'form-select form-select-sm'}))
    
    class Meta:
        model = Category
        fields = ("software","type_software","tasks","type_public","type_industry")
        
        widgets = {
            "software":forms.Select(attrs={'style':'display:none;'}),
            "type_software": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "type_public": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "type_industry": forms.Select(attrs={
                'class':'form-select form-select-sm js-example-basic-single',
            })
        }


#form version of software
class SoftwareVersionForm(forms.ModelForm):

    class Meta:
        model = Software
        fields = ["slug","version","date_created","origin_country"]
                
        widgets = {
            "slug": forms.TextInput(attrs={'style':'display:none;'}),
            "version": forms.TextInput(attrs={'style':'display:none;'}),
            "date_created": forms.DateInput(attrs={'class':'form-control p-3 shadow', "type":'date'}),
            "origin_country": forms.TextInput(attrs={'class':'form-control shadow p-3', 'value':'COLOMBIA'}),
        }


#origin work of software
class SoftwareOriginForm(forms.ModelForm):

    class Meta:
        model = Software
        fields = ["slug","type_of_work"]

        widgets = {
            "slug": forms.TextInput(attrs={'style':'display:none;'}),
            "type_of_work": forms.RadioSelect(attrs={}),
        }
       
#
class DescriptionForm(forms.ModelForm):
    
    class Meta:
        model = Software
        fields = ("description",)
        
        widgets = {
            "user":forms.Select(attrs={'style':'display:none;'}),
            "description": forms.Textarea(attrs={'class':'form-control',"rows":"4","cols":"50"}),
            "date_created": forms.DateInput(attrs={'class':'form-control','type':'date'}),
            "version": forms.TextInput(attrs={'class':'form-control'})
        }

# form requeriment
class RequerimentForm(forms.ModelForm):
    
    class Meta:
        model = Requeriment
        fields = ("software","name","description","version","image")
        
        widgets = {
            "software":forms.Select(attrs={'style':'display:none;'}),
            "name": forms.TextInput(attrs={
                'class':'form-control form-control p-3 fw-bold shadow',
                'placeholder':'Nombre de la Interfaz',
                }),
            "description": forms.Textarea(attrs={
                'class':'form-control shadow',
                'maxlength':'350',
                'cols':"80",
                'rows':"4"
                }),
        }


#form para validar la informacion de tipo de publico objectivo para presentar el manual de usuario
class SoftwarePublicForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ("type_public","level_public")
        
        widgets = {
            "type_public": forms.RadioSelect(),
            "level_public": forms.RadioSelect()
            
        }

#form para validar la informacion del autor
class AuthorsForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ('software','first_name','second_name','last_name','type_ID','num_ID','nacionality','email')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            'second_name': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            'last_name': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            # 'type_ID': forms.se(attrs={'class':'form-control shadow p-3'}),
            'num_ID': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            'nacionality': forms.TextInput(attrs={'class': 'form-control shadow p-3', 'value':'COLOMBIA'}),
            # 'address': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            # 'phone': forms.TextInput(attrs={'class':'form-control shadow p-3'}),
            'email': forms.TextInput(attrs={'class':'form-control shadow p-3'})
        }

