from django.db import models
from django.urls import reverse

from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.
class App(models.Model):
    name = models.CharField(("nombre aplicacion"), max_length=50, unique=True)
    logo = models.ImageField(("logo"), upload_to="uploads", blank=True, null=True)
    slug = models.SlugField("slug")
    thumbnail = models.ImageField(upload_to="uploads", blank=True, null=True)
    

    class Meta:
        verbose_name = ("App")
        verbose_name_plural = ("Apps")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("App_detail", kwargs={"pk": self.pk})
    
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
    
    def make_thumbnail(self, image, size=(200, 50)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

#models auxialiares
class Template(models.Model):
    name = models.CharField(("nombre"), max_length=150, unique=True)
    description = models.TextField(("description"), blank=False, null=False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Template")
        verbose_name_plural = ("Templates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Template_detail", kwargs={"pk": self.pk})
