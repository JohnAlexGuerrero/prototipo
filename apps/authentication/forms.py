from django import forms

from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser, Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email'})
    )
    username = forms.CharField(
        label="username",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'})
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})
    )
    password2 = forms.CharField(
        label="Comfirmation password",
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})
    )
    first_name = forms.CharField(
        label="Primer nombre",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'})
    )
    second_name = forms.CharField(
        label="Segundo nombre",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your second name'})
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last_name'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['email','username','password1','password2','first_name','second_name','last_name']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['occupation','institution','profession_career','gender','avatar']

        widgets = {
            "avatar": forms.FileInput(attrs={'class':'d-none'}),
            "gender": forms.RadioSelect(),
        }