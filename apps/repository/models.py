from django.urls import reverse
from django.utils.text import slugify

from django.db import models
from authentication.models import CustomUser

# Create your models here.

class License(models.IntegerChoices):
    PROPERTY = 1, "Propietario"
    FREE_CODE = 2, "Libre"
    OPEN_CODE = 3, "Código Abierto"
    
class Software(models.Model):
    title = models.CharField(("Software titulo"), max_length=150, null=False, unique=True)
    description = models.TextField(("descripción"), max_length=250, null=False)
    version = models.CharField(("version"), max_length=50, null=False)
    license = models.PositiveSmallIntegerField(("tipo de licencia"), choices=License.choices, default=License.PROPERTY)
    slug = models.SlugField()
    user = models.ForeignKey(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Software")
        verbose_name_plural = ("Softwares")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Software_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)