from django.urls import reverse
from django.utils.text import slugify
from django_countries import countries
from ckeditor.fields import RichTextField

from django.db import models
from authentication.models import CustomUser

import re

# Create your models here.

class TypeOfWork(models.TextChoices):
    OBRA_INEDITA = "Obra inédita"
    OBRA_DERIVADA = "Obra derivada"

class TypeFunctionSoftware(models.TextChoices):
    PRODUCTIVIDAD = "Software de productividad"
    MULTIMEDIA =  "Software de multimedia"
    JUEGOS = "Juegos"
    INTERNET = "Internet"
    HERRAMIENTAS_Y_LIBRERIAS = "Herramientas y librerias"
    PROGRAMACION = "Herramientas de desarrollo"
    LENGUAJES_DE_PROGRAMACION = "Lenguaje de programación"
    DEVOPS = "Herramientas Devops"
    BASES_DE_DATOS = "Bases de datos"

class TypePublic(models.TextChoices):
    APTO_PARA_TODO_PUBLICO = "Apto para todo público"
    ADOLESCENTES = "Adolecentes"
    MAYORES_DE_17_AÑOS = "Mayores de 17 años"    
    
class Task(models.TextChoices):
    # GESTION_DE_ARCHIVOS_Y_CARPETAS = 'Gestion De Archivos y carpetas'
    # PROCESAMIENTO_DE_TEXTOS = 'Procesamiento de textos'
    CALCULO_Y_ANALISIS_DE_DATOS = 'Calculo Y Analisis De Datos'
    # GESTION_BASES_DATOS = 'Gestion bases de datos'
    # COMUNICACION_COLABORACION = 'Comunicación y colaboración'
    # REPRODUCCION_MULTIMEDIA_DE_AUDIO_Y_VIDEO = 'Reproducción multimedia de audio y video'
    # CREACION_CONTENIDO_MULTIMEDIA = 'Creacion de contenido multimedia'
    # JUEGOS = 'Juegos'
    # NAVEGADORES_WEB = 'Navegadores web'
    # MESANGERIA = 'Mensajeria'
    # GESTION_DE_DISPOSITIVOS = 'Gestion de dispositivos'
    # AUTOMATIZACION_DE_TAREAS = 'Automatizacion de tareas'
    # SEGURIDAD_INFORMATICA = 'Seguridad informatica'
    COMPRESOR_DE_ARCHIVOS = 'Compresor De Archivos'
    # GESTION_DEL_TIEMPO = 'Gestion del tiempo'
    # TRADUCCION_DE_IDIOMAS = 'Traduccion de idiomas'
    # EDUCACION_Y_APRENDIZAJE = 'Educacion y aprendizaje'
    # DISEÑO_Y_MODELADO = 'Diseño y modelado'
    # GESTION_DE_PROYECTOS = 'Gestion de proyectos'
    # CONTABILIDAD_Y_FINANZAS = 'Contabilidad y finanzas'
    # GESTION_DE_RELACIONES_CON_CLIENTES_CRM = 'Gestion de relaciones con clientes CRM'
    # BUSINESS_INTELLIGENCE_BI = 'Business Intelligence BI'
    # E_COMMERCE = "E commerce"
    MINERIA_DE_DATOS = "Mineria De Datos"

class Sector(models.TextChoices):
    SALUD = "Salud"
    EDUCACION = "Educación"
    FINANZAS_Y_ECONOMIA = "Finanzas y economia"
    MANUFACTURA = "Manufactura"
    TRANSPORTE_Y_LOGISTICA = "Transporte y logistica"
    AGRICULTURA = "Agricultura"
    GOBIERNO = "Gobierno"
    TELECOMUNICACIONES = "Telecomunicaciones"
    ENERGIA = "Energía"
    RECURSOS_HUMANOS = "Recursos Humanos"
    MARKETING = "Marketing"
    LEGAL = "Legal"
    CONSTRUCCION = "Construcción"
    TURISMO = "Turismo"
    BIENES_RAICES =	"Bienes Raíces"
    ENTRETENIMIENTO = "Entretenimiento"
    DEPORTES = "Deportes"
    CIENCIA_E_INVESTIGACION = "Ciencia e investigación"
    SERVICIOS_PUBLICOS = "Servicios Publicos"

class Software(models.Model):
    title = models.CharField(("Software titulo"), max_length=150, null=False, unique=True)
    description = models.CharField(("description"), max_length=150)
    version = models.CharField(("version"), max_length=50, null=False)
    slug = models.SlugField()
    user = models.ForeignKey(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    date_created = models.DateField(("Fecha de creación"), auto_now_add=False, blank=True, null=True)
    type_of_work = models.CharField(("El software es"), max_length=50, choices=TypeOfWork.choices, default=TypeOfWork.OBRA_DERIVADA)
    origin_country = models.CharField(("nacionalidad"), max_length=50, null=True, blank=True)
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
    license = models.CharField(("tipo de licencia"), max_length=150, null=True, blank=True)
    type_software = models.CharField(("Tipo de software"), max_length=150,choices=TypeFunctionSoftware.choices, null=True, blank=True)
    tasks = models.TextField(("tareas"), max_length=255, blank=True,null=True)
    type_public = models.CharField(("Tipo de audiencia"), max_length=100, choices=TypePublic.choices, default=TypePublic.APTO_PARA_TODO_PUBLICO)
    type_industry = models.CharField(("sector"), max_length=100, choices=Sector.choices,null=True, blank=True)
    os = models.CharField(("sistema operativo"), max_length=250, blank=True, null=True)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.software.title

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if self.tasks is not None:
            self.tasks = self.tasks.strip("[]")
            for item in self.tasks.split(','):
                print(item)
            print(self.tasks)
        return super().save(*args, **kwargs)
    
    def get_tasks_list(self):
        list_tasks = [x for x in self.tasks.split(',')]
        return list_tasks

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

