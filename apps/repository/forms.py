from django_countries.data import COUNTRIES
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django import forms

from repository.models import Software
from repository.models import Category
from authentication.models import CustomUser

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("software","type_software","type_public","type_industry","os")
        
        widgets = {
            "software": forms.Select(attrs={'class':'border-0 bg-body-secondary form-select form-select-sm'}),
            "type_software": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "type_public": forms.RadioSelect(attrs={'class':'form-ckeck-input'}),
            "type_industry": forms.Select(attrs={
                'class':'form-select form-select-sm js-example-basic-single',
            }),
            "os": forms.Select(attrs={
                'class':'form-control js-example-basic-single',
                'placeholder': 'Selecciona los sistemas operativos',
            })
        }


class SoftwareNewForm(forms.ModelForm):
    origin_country = CountryField().formfield()
    
    class Meta:
        model = Software
        fields = ['user','title','description','version','license','date_created','type_of_work','origin_country']
        
        widgets = {
            # "user": forms.Select(attrs={'style':'display:none;'}),
            "title": forms.TextInput(attrs={
                'class':'form-control form-control-sm',
            }),
            "description":forms.Textarea(attrs={
                'class':'form-control',
                "placeholder":"Indique únicamente las Funciones Técnicas realizadas por el soporte lógico software (ej. Compila, almacena, genera reportes, automatiza datos, procesa datos, organiza datos, gestiona y registra, controla, produce, crea reportes, etc.)",
                "cols":"50",
                "rows":"3"
            }),
            "version": forms.TextInput(attrs={
                'class':'form-control form-control-sm w-75',
                'placeholder':'ejemplo: v1.0'
            }),
            "license": forms.RadioSelect(),
            "type_of_work": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "date_created": forms.DateInput(attrs={'class':'form-control w-100', 'type':"date"}),
            "origin_country": CountrySelectWidget()
        }
        
    def __init__(self, *args, **kwargs):
        super(SoftwareNewForm, self).__init__(*args, **kwargs)
        print(kwargs)
        # self.fields['user'].initial = user

