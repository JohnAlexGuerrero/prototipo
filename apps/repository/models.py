from django.urls import reverse
from django.utils.text import slugify
from django_countries import countries
from ckeditor.fields import RichTextField

from io import BytesIO
from PIL import Image
from django.core.files import File

from django.db import models
from authentication.models import Profile

import re

# Create your models here.



class TypeOfWork(models.TextChoices):
    SOFTWARE_INEDITO = "Software Inedito"
    SOFTWARE_DERIVADO = "Software Derivado"

class TypeFunctionSoftware(models.TextChoices):
    PRODUCTIVIDAD = "Software de productividad ayuda a los usuarios a realizar tareas comunes de manera más eficiente."
    CREATIVIDAD =  "Software de creatividad ayuda a los usuarios a crear contenido multimedia, como imágenes, videos y música."
    COMUNICACION = "El software de comunicación ayuda a los usuarios a comunicarse con otros."
    NEGOCIOS = "El software empresarial ayuda a las empresas a realizar sus operaciones."
    PROGRAMACION = "El software de programación ayuda a los desarrolladores a crear distintas aplicaciones."
    ENTRETENIMIENTO = "El software de entretenimiento ayuda a los usuarios a relajarse y divertirse."
    EDUCACION = "El software educativo ayuda a los usuarios a aprender cosas nuevas."
    BIENESTAR_Y_SALUD = "El software de bienestar se enfoca en el cuidado de la salud de los usuarios."

class TypePublic(models.TextChoices):
    APTO_PARA_TODO_PUBLICO = "Apto para todo público"
    ADOLESCENTES = "Adolecentes"
    MAYORES_DE_17_AÑOS = "Mayores de 17 años"    
    
class Task(models.TextChoices):
    ANTHIVIRUS = 'Anthivirus'
    BUSINESS_INTELLIGENCE_BI = 'Business Intelligence BI'
    CUIDADO_DE_MASCOTAS = 'Cuidado De Mascotas'
    CALCULO_Y_ANALISIS_DE_DATOS = 'Calculo Y Analisis De Datos'
    CORREO_ELECTRONICO = 'Correo Electronico'
    CREACION_DE_CONTENIDO_MULTIMEDIA = 'Creacion De Contenido Multimedia'
    CREACION_DE_DOCUMENTOS = 'Creacion De Documentos'
    CALENDARIOS = 'Calendarios'
    COMPRESOR_DE_ARCHIVOS = 'Compresor De Archivos'
    CURSOS_EN_LINEA = 'Cursos En Linea'
    CONTABILIDAD_Y_FINANZAS = 'Contabilidad Y Finanzas'
    DESARROLLO_DE_SOFTWARE = 'Desarrollo De Software'
    DISEÑO_GRAFICO = 'Diseño Grafico'
    DISEÑO_Y_MODELADO = 'Diseño Y Modelado'
    EDUCACION_Y_APRENDIZAJE = 'Educacion Y Aprendizaje'
    EDITORES_DE_IMAGENES = 'Editores De Imagenes'
    E_COMMERCE = "E commerce"
    EDITORES_DE_VIDEO = 'Editores De Video'
    GESTION_BASES_DATOS = 'Gestion Bases De Datos'
    GESTION_DE_ARCHIVOS_Y_CARPETAS = 'Gestion De Archivos y carpetas'
    GESTION_DE_DISPOSITIVOS = 'Gestion De Dispositivos'
    GESTION_DE_TAREAS = 'Gestion De Tareas'
    HOJAS_DE_CALCULO = 'Hojas De Calculo'
    GESTION_DE_RELACIONES_CON_CLIENTES_CRM = 'Gestion De Relaciones Con Clientes CRM'
    GESTION_DEL_TIEMPO = 'Gestion Del Tiempo'
    GESTION_DE_PROYECTOS = 'Gestion De Proyectos'
    HERRAMIENTAS_EDUCATIVAS = 'Herramientas Educativas'
    HERRAMIENTAS_DE_MINERIA_DE_DATOS = "Herramientas De Mineria De Datos"
    HERRAMIENTAS_DE_INTELIGENCIA_ARTIFICIAL = "Herramientas De Inteligencia Artificial"
    JUEGOS = 'Juegos'
    LIBROS_ELECTRONICOS = 'Libros Electronicos'
    MESANGERIA_INSTANTANEA = 'Mensajeria Instantanea'
    NOTAS = 'Notas'
    NAVEGADORES_WEB = 'Navegadores Web'
    PRESENTACIONES = 'Presentaciones'
    PROCESAMIENTO_DE_TEXTOS = 'Procesamiento De Textos'
    REDES_SOCIALES = 'Redes Sociales'
    REPRODUCCION_MULTIMEDIA_DE_AUDIO_Y_VIDEO = 'Reproducción Multimedia De Audio Y Video'
    SOFTWARE_DE_MUSICA = 'Software_De_Musica'
    SERVICIOS_DE_TRANSMISION = 'Servicios De Transmision'
    SOFTWARE_DE_IDIOMAS = 'Software De Idiomas'
    SALUD_Y_CUIDADO_PERSONAL = 'Salud Y Cuidado Personal'
    SEGURIDAD_INFORMATICA = 'Seguridad Informatica'
    TRADUCCION_DE_IDIOMAS = 'Traduccion De Idiomas'
    VIDEOLLAMADAS = 'Videollamadas'

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
    SOFTWARE = "Desarrollo de Software"

class TypePublicLevel(models.TextChoices):
    PRINCIPIANTE = "Usuarios con poco o ningún conocimiento previo sobre el software o el tipo de tecnología relacionada."
    INTERMEDIO = "Usuarios con conocimiento básico del software o la tecnología relacionada y puede realizar tareas básicas."
    EXPERTO = "Usuarios con conocimiento profundo del software o la tecnología relacionada y puede realizar tareas complejas."

class Software(models.Model):
    title = models.CharField(("Software titulo"), max_length=150, null=False, unique=True)
    description = models.TextField(("description"), blank=True, null=True)
    version = models.CharField(("version"), max_length=50, null=False)
    slug = models.SlugField()
    user = models.ForeignKey(Profile, verbose_name=("user"), on_delete=models.CASCADE)
    date_created = models.DateField(("Fecha de creación"), auto_now_add=False, blank=True, null=True)
    type_of_work = models.CharField(("El software es"), max_length=50, choices=TypeOfWork.choices, default=TypeOfWork.SOFTWARE_DERIVADO)
    origin_country = models.CharField(("nacionalidad"), max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Software")
        verbose_name_plural = ("Softwares")

    def __str__(self):
        return self.title
    
    def get_authors(self):
        return Author.objects.filter(software__slug=self.slug)

    def get_absolute_url(self):
        return reverse("Software_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_requeriments(self):
        return Requeriment.objects.all().filter(software_id=self.id)
    
    def get_logo(self):
        if self.logo:
            return 'http://127.0.0.1:8000' + self.logo.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.logo:
                self.thumbnail = self.make_thumbnail(self.logo)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
                            
class Category(models.Model):
    software = models.OneToOneField(Software, verbose_name=("software"), on_delete=models.CASCADE)
    license = models.CharField(("tipo de licencia"), max_length=150, null=True, blank=True)
    type_software = models.CharField(("Tipo de software"), max_length=150,choices=TypeFunctionSoftware.choices, null=True, blank=True)
    tasks = models.TextField(("tareas"), max_length=255, blank=True,null=True)
    type_public = models.CharField(("Tipo de audiencia"), max_length=100, choices=TypePublic.choices, default=TypePublic.APTO_PARA_TODO_PUBLICO)
    level_public = models.CharField(("Nivel de conocimiento"), max_length=200, choices=TypePublicLevel.choices, default=TypePublicLevel.PRINCIPIANTE)
    type_industry = models.CharField(("sector"), max_length=200, choices=Sector.choices,null=True, blank=True)
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
            self.tasks = self.tasks.strip("['/']")
        return super().save(*args, **kwargs)
    
    def get_tasks_list(self):
        list_tasks = [x for x in self.tasks.split(',')]
        return list_tasks

#requerimientos de sistema
class Requeriment(models.Model):
    software = models.ForeignKey(Software, verbose_name=("software"), on_delete=models.CASCADE)
    name = models.CharField('titulo', max_length=50,null=False,blank=False)
    description = models.TextField(("descripción"), null=True, blank=True)
    slug = models.SlugField()
    image = models.ImageField(("uploads"), blank=True, null=True)
    thumbnail = models.ImageField(("uploads"), blank=True, null=True)
    version = models.CharField(("versión"), max_length=50, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Requeriment")
        verbose_name_plural = ("Requeriments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("requeriment_edit", kwargs={"software_slug": self.software.slug, "requeriment_slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
          
    
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

#arquitectura de sistema
class Arquitect(models.Model):
    software = models.OneToOneField(Software, verbose_name=("software"), on_delete=models.CASCADE)
    name = models.CharField(("nombre"), max_length=50, unique=True)
    description = models.CharField(("descripcion"), max_length=250, null=False)
    image = models.ImageField(("Imagen"), upload_to="images/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Arquitect")
        verbose_name_plural = ("Arquitects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Arquitect_detail", kwargs={"pk": self.pk})

#model installation
class Installation(models.Model):
    software = models.ForeignKey(Software, verbose_name=("software"), on_delete=models.CASCADE)
    platform = models.CharField(("plataforma"), max_length=150)
    os = models.CharField(("sistema operativo"), max_length=250, blank=True, null=True)
    procesador = models.CharField(("sistema operativo"), max_length=250, blank=True, null=True)
    ram = models.CharField(("sistema operativo"), max_length=250, blank=True, null=True)
    storage = models.CharField(("siste"), max_length=250, blank=True, null=True)
    screen = models.CharField(("resolución de pantalla"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("Installation")
        verbose_name_plural = ("Installations")

    def __str__(self):
        return self.software.title

    def get_absolute_url(self):
        return reverse("Installation_detail", kwargs={"pk": self.pk})

#model solicitar certificado de derecho de autor
class CopyrightCertificate(models.Model):
    software = models.ForeignKey(Software, verbose_name=("software"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("CopyrightCertificate")
        verbose_name_plural = ("CopyrightCertificates")

    def __str__(self):
        return self.software

    def get_absolute_url(self):
        return reverse("CopyrightCertificate_detail", kwargs={"pk": self.pk})


# model para la entidad author
class Author(models.Model):
    software = models.ForeignKey(Software, verbose_name=("software"), on_delete=models.CASCADE)
    first_name = models.CharField(("Primer Nombre"), max_length=150, null=False, blank=False)
    second_name = models.CharField(("Segundo Nombre"), max_length=150, null=True, blank=True)
    last_name = models.CharField(("Apellidos"), max_length=150, null=False, blank=False)
    type_ID = models.CharField(("Tipo de Documento"), max_length=50, null=False, blank=False)
    num_ID = models.CharField(("Numero de Documento"), max_length=50, null=False, blank=False)
    born_date = models.DateField(("Fecha de Nacimiento"), auto_now=False, blank=True, null=True)
    nacionality = models.CharField(("Nacionalidad"), max_length=50, default='COLOMBIA')
    address = models.CharField(("Direccion"), max_length=150, blank=True, null=True)
    email = models.EmailField(("Email"), max_length=254, blank=False, null=False)
    phone = models.CharField(("Telefono"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})
