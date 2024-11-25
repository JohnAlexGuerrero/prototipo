from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Profile(AbstractUser):
    class Gender(models.TextChoices):
        MAN = "Hombre" 
        WOMAN = "Mujer"

    class Rol(models.TextChoices):
        TEACHER = "PROFESOR", "Profesor"
        STUDENT = "ESTUDIANTE", "Estudiante"
        
    email = models.EmailField(max_length=150, unique=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    second_last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=30, choices=Gender.choices, blank=True, null=True)
    phone = models.CharField(("número de teléfono"), max_length=50, blank=True, null=True)
    rol = models.CharField(max_length=50, choices=Rol.choices, blank=True, null=True)
    institute = models.CharField(max_length=50, blank=True, null=True)
    profession = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    #campo identificador unico del User
    USERNAME_FIELD = 'email'
    
    #forzar a introducir un campo
    REQUIRED_FIELDS = ['username','password']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
         