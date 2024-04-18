from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    second_last_name = models.CharField(max_length=50, blank=True, null=True)
    
    #campo identificador unico del User
    USERNAME_FIELD = 'email'
    
    #forzar a introducir un campo
    REQUIRED_FIELDS = ['username','password']
    
    def __str__(self):
        return self.username

class Rol(models.IntegerChoices):
    STUDENT = 1, "Estudiante"
    TEACHER = 2, "Profesor"

class Institute(models.IntegerChoices):
    CESMAG = 1, "Universidad Cesmag"
    UDENAR = 2, "Universidad de Nariño"
    UNIMAR = 3, "Universidad Mariana"
    UCC = 4, "Universidad Coperativa de Colombia"
    UNAD = 5, "Universidad Nacional Abierta y a Distancia"
    UAN = 6, "Universidad Antonio Nariño"
    SENA = 7, "Servicio Nacional de Aprendizaje"
    
class ProfessionCareer(models.IntegerChoices):
    SYSTEM_INGEENIER = 1, "Ingeniero de Sistemas"
    ELECTRONIC_INGEENIER = 2, "Ingeniero Electrónico"
    SYSTEM_TECH = 3, "Tecnología en Sistemas"
    
class Gender(models.IntegerChoices):
    MAN = 1, "Hombre" 
    WOMAN = 2, "Mujer"
         
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", default='no_picture.jpg')
    gender = models.SmallIntegerField(choices=Gender.choices, blank=True, null=True)
    slug = models.SlugField()
    occupation = models.PositiveSmallIntegerField(choices=Rol.choices, default=Rol.STUDENT)
    institution = models.PositiveSmallIntegerField(choices=Institute.choices, blank=True, null=True)
    profession_career = models.PositiveSmallIntegerField(choices=ProfessionCareer.choices, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)
