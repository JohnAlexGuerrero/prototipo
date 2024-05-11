from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from django import forms
from django.forms import MultipleChoiceField

from repository.models import Software, Requeriment
from repository.models import Category, Task
from authentication.models import CustomUser

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

#form of new software
class SoftwareNewForm(forms.ModelForm):
    
    class Meta:
        model = Software
        fields = ['user','title','description']
        
        widgets = {
            "title": forms.TextInput(attrs={
                'class':'form-control form-control-sm shadow',
            }),
            "description":forms.Textarea(attrs={
                'class':'form-control shadow form-control-sm',
                "placeholder":"",
                "rows":"8",
                "cols":"10"
            })
        }

#form version of software
class SoftwareVersionForm(forms.ModelForm):
    origin_country = CountryField().formfield()

    class Meta:
        model = Software
        fields = ["slug","version","date_created","origin_country"]
                
        widgets = {
            "slug": forms.TextInput(attrs={'style':'display:none;'}),
            "version": forms.TextInput(attrs={'style':'display:none;'}),
            "date_created": forms.DateInput(attrs={'class':'form-control form-control-sm', "type":'date'}),
            "origin_country": CountrySelectWidget(),
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
        fields = ("user","description","version","date_created")
        
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
        fields = ("software","name","description","version")
        
        widgets = {
            "software":forms.Select(attrs={'style':'display:none;'}),
            "name": forms.TextInput(attrs={'class':'form-control form-control-sm p-2 shadow'}),
            "description": forms.Textarea(attrs={'class':'form-control form-control-sm shadow'}),
        }

