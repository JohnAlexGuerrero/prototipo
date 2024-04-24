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

set_semester = (
    (1,"I"),
    (2,"II"),
    (3,"III"),
    (4,"IV"),
    (5,"V"),
    (6,"VI"),
    (7,"VII"),
    (8,"VIII"),
    (9,"IX"),
    (10,"X")
)
class Rol(models.TextChoices):
    TEACHER = "PROFESOR", "Profesor"
    STUDENT = "ESTUDIANTE", "Estudiante"

class Institute(models.TextChoices):
    CESMAG = "CESMAG", "Universidad Cesmag"
    UDENAR = "UDENAR", "Universidad de Nariño"
    UNIMAR = "UNIMAR", "Universidad Mariana"
    UCC = "UCC", "Universidad Coperativa de Colombia"
    UNAD = "UNAD", "Universidad Nacional Abierta y a Distancia"
    UAN = "UAN", "Universidad Antonio Nariño"
    SENA = "SENA", "Servicio Nacional de Aprendizaje"
    
class ProfessionCareer(models.TextChoices):
    SYSTEM_INGEENIER = "Ing. Sistemas", "Ingeniero de Sistemas"
    ELECTRONIC_INGEENIER = "Ing. Electrónica", "Ingeniero Electrónico"
    SYSTEM_TECH = "Tecnología en sistemas", "Tecnología en Sistemas"
    
class Gender(models.IntegerChoices):
    MAN = 1, "Hombre" 
    WOMAN = 2, "Mujer"
         
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", default='no_picture.jpg')
    gender = models.SmallIntegerField(choices=Gender.choices, blank=True, null=True)
    phone = models.CharField(("número de teléfono"), max_length=50, blank=True, null=True)
    slug = models.SlugField()
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

class Academica(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    university = models.CharField(("Universidad"), max_length=50, choices=Institute.choices, blank=True, null=True)
    rol = models.CharField(("Rol"), max_length=50, choices=Rol.choices)
    profession = models.CharField(("Carrera profesional"), max_length=150, choices=ProfessionCareer.choices, blank=True, null=True)
    semester = models.IntegerField(("semestre"), choices=set_semester, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Academica")
        verbose_name_plural = ("Academicas")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Academica_detail", kwargs={"slug": self.user.username})
