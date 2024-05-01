from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms
from django.forms import MultipleChoiceField

from repository.models import Software
from repository.models import Category, Task
from authentication.models import CustomUser

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


class SoftwareNewForm(forms.ModelForm):
    # origin_country = CountryField().formfield()
    
    class Meta:
        model = Software
        fields = ['user','title','description']
        
        widgets = {
            "title": forms.TextInput(attrs={
                'class':'form-control form-control-sm',
            }),
            "description":forms.Textarea(attrs={
                'class':'form-control',
                "placeholder":"",
                "rows":"5",
                "cols":"10"
            }),
            # "version": forms.TextInput(attrs={
            #     'class':'form-control form-control-sm w-75',
            #     'placeholder':'ejemplo: v1.0'
            # }),
            # "license": forms.RadioSelect(),
            # "type_of_work": forms.Select(attrs={'class':'form-select form-select-sm'}),
            # "date_created": forms.DateInput(attrs={'class':'form-control w-100', 'type':"date"}),
            # # "origin_country": CountrySelectWidget()
            # "logo": forms.FileInput(attrs={'class':'form-control form-control-sm'})
        }
        

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
