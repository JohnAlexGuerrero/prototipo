from django.urls import reverse
from django.utils.text import slugify
from django_countries import countries
from ckeditor.fields import RichTextField

from django.db import models
from authentication.models import CustomUser

# Create your models here.

class License(models.TextChoices):
    PROPERTY = "PROPIETARIO", "Software propietario"
    # FREE_CODE = "CODIGO LIBRE", "Software libre"
    OPEN_SOURCE = "CÓDIGO ABIERTO", "Software de Código Abierto"

class TypeOfWork(models.IntegerChoices):
    UNPUBLISHED = 1, "Obra inédita"
    DERIVED = 2, "Obra derivada"

class TypeFunctionSoftware(models.IntegerChoices):
    APPLICATION = 1, "Software de aplicación"
    PROGRAMMING = 2, "Software de programación"
    SYSTEM = 3, "Software de sistema"

class TypePublic(models.IntegerChoices):
    ALL_PUBLIC = 1, "Apto para todo público"
    TEENAGERS = 2, "Adolecentes"
    ADULT = 3, "Mayores de 17 años" 

class Sector(models.IntegerChoices):
    HEALTH = 1,	"Salud"
    EDUCATION = 2,	"Educación"
    FINANCE = 3, "Finanzas"
# 4	Manufactura
# 5	Retail
# 6	Transporte y logística
# 7	Agricultura
# 8	Gobierno
# 9	Telecomunicaciones
# 10	Energía
# 11	Recursos Humanos
# 12	Marketing
# 13	Legal
# 14	Construcción
# 15	Turismo
# 16	Bienes Raíces
# 17	Entretenimiento
# 18	Deportes
# 19	Ciencia e investigación
# 20	Servicios Públicos
# 1 Health
# 2 Education
# 3 Finance
# 4 Manufacturing
# 5 Retail
# 6 Transportation and logistics
# 7 Agriculture
# 8 Government
# 9 Telecommunications
# 10 Energy
# 11 Human Resources
# 12 Marketing
# 13 Legal
# 14 Construction
# 15 Tourism
# 16 Real Estate
# 17 Entertainment
# 18 Sports
# 19 Science and research
# 20 Public Services

class Software(models.Model):
    title = models.CharField(("Software titulo"), max_length=150, null=False, unique=True)
    description = models.CharField(("description"), max_length=150)
    version = models.CharField(("version"), max_length=50, null=False)
    slug = models.SlugField()
    user = models.ForeignKey(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    date_created = models.DateField(("Fecha de creación"), auto_now_add=False, blank=True, null=True)
    # type_of_work = models.PositiveSmallIntegerField(("El software es"), choices=TypeOfWork.choices, default=TypeOfWork.UNPUBLISHED)
    # origin_country = models.CharField(("country"), max_length=50, null=True, blank=True)
    logo = models.ImageField("logo", upload_to="logos/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Software")
        verbose_name_plural = ("Softwares")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Software_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
                            
class Category(models.Model):
    software = models.OneToOneField(Software, verbose_name=("software"), on_delete=models.CASCADE)
    license = models.TextField(("tipo de licencia"), max_length=150, choices=License.choices, null=True, blank=True)
    type_software = models.TextField(("Tipo de software por funcionalidad"), max_length=150,choices=TypeFunctionSoftware.choices, null=True, blank=True)    
    type_public = models.PositiveSmallIntegerField(("Tipo de audiencia"), choices=TypePublic.choices, null=True, blank=True)
    type_industry = models.PositiveSmallIntegerField(("sector"), choices=Sector.choices,null=True, blank=True)
    # functions = models.CharField("functions", max_length=250, choices=Sector.choices)
    os = models.CharField(("sistema operativo"), max_length=250, blank=False, null=False)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.software.title

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Requeriment(models.Model):
    software = models.ForeignKey(Software, verbose_name=("software"), on_delete=models.CASCADE)
    description = models.TextField(("descripción"), null=True, blank=True)
    version = models.CharField(("versión"), max_length=50, null=False)
    priority = models.PositiveBigIntegerField(("prioridad"), max_length=50, choices=[(1,"Alta"),(2,"Media"),(3,"Baja")])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Requeriment")
        verbose_name_plural = ("Requeriments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Requeriments_detail", kwargs={"pk": self.pk})

class Funtionality(models.Model):
    requeriment = models.ForeignKey(Requeriment, verbose_name=("requeriment"), on_delete=models.CASCADE)
    description = models.CharField(("description"), max_length=150, null=False)

    class Meta:
        verbose_name = ("Funtionality")
        verbose_name_plural = ("Funtionalities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Funtionality_detail", kwargs={"pk": self.pk})

