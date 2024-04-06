from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    
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
    NOT_GENDER = 1, "Sin especificar" 
    MAN = 2, "Hombre" 
    WOMAN = 3, "Mujer"
         
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", default='no_picture.jpg')
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.NOT_GENDER)
    slug = models.SlugField(blank=True, null=True)
    occupation = models.PositiveSmallIntegerField(choices=Rol.choices, default=Rol.STUDENT)
    institution = models.PositiveSmallIntegerField(choices=Institute.choices, default=Institute.CESMAG)
    profession_career = models.PositiveSmallIntegerField(choices=ProfessionCareer.choices, default=ProfessionCareer.SYSTEM_INGEENIER)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user
        return super().save(*args, **kwargs)
