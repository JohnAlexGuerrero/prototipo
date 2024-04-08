from django_countries import countries
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms

from repository.models import Software

class SoftwareNewForm(forms.ModelForm):
    origin_country = CountryField().formfield()
    
    class Meta:
        model = Software
        fields = ['user','title','description','version','license','date_created','type_of_work','origin_country']
        
        widgets = {
            "user": forms.Select(attrs={'class':'border-0 bg-body-secondary form-select form-select-sm'}),
            "title": forms.TextInput(attrs={
                'class':'form-control form-control-sm',
            }),
            "description":forms.TextInput(attrs={
                'class':'form-control',
                "placeholder":'describe',
            }),
            "version": forms.TextInput(attrs={
                'class':'form-control form-control-sm w-75',
                'placeholder':'ejemplo: v1.0'
            }),
            "license": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "type_of_work": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "date_created": forms.DateInput(attrs={'class':'form-control w-100', 'type':"date"}),
            "origin_country": CountrySelectWidget()
        }

