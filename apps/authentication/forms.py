from typing import Any, Mapping
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from authentication.models import CustomUser, Profile, Academica

#formulario para el registro de un nuevo usuario
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control shadow', 'placeholder':'Enter email'})
    )
    username = forms.CharField(
        label="username",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Enter username'})
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class':'form-control shadow','type':'password'})
    )
    password2 = forms.CharField(
        label="Comfirmation password",
        widget=forms.PasswordInput(attrs={'class':'form-control shadow','type':'password'})
    )
    first_name = forms.CharField(
        label="Primer nombre",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Enter your name'})
    )
    second_name = forms.CharField(
        label="Segundo nombre",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Enter your second name'})
    )
    last_name = forms.CharField(
        label="Primer apellido",
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Enter your last_name'})
    )
    second_last_name = forms.CharField(
        label="Segundo apellido",
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control shadow', 'placeholder':'Enter your last_name'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['email','username','password1','password2','first_name','second_name','last_name','second_last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender','avatar','phone']

        widgets = {
            "avatar": forms.FileInput(attrs={'style':'display:none;color:red;'}),
            "gender": forms.RadioSelect(),
        }

class CustomUserEditForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ("username","email",)


class AcademicaForm(forms.ModelForm):
    class Meta:
        model = Academica
        fields = ['user','university','rol','profession','semester']
        
        widgets = {
            "user": forms.Select(attrs={}),
            "university": forms.Select(attrs={'class':'form-select form-select-sm mb-3'}),
            "rol": forms.RadioSelect(),
            "profession": forms.Select(attrs={'class':'form-select form-select-sm mb-3'}),
            "semester": forms.Select(attrs={'class':'form-select form-select-sm mb-3'})
        }

class AcademicaRoleForm(forms.ModelForm):
    class Meta:
        model = Academica
        fields = ['user','rol']

class AcademicaUniversityForm(forms.ModelForm):
    
    class Meta:
        model = Academica
        fields = ("university","profession","semester")
        
        widgets = {
            "university": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "profession": forms.Select(attrs={'class':'form-select form-select-sm'}),
            "semester": forms.Select(attrs={'class':'form-select form-select-sm'})
        }


class ProfileContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["gender","phone"]
        
        widgets = {
            "gender":forms.Select(attrs={'class':'form-select form-select-sm'}),
            "slug": forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            "phone": forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'555-5555-555'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProfileContactForm, self).__init__(*args, **kwargs)

