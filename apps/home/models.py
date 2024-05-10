from django.db import models
from django.urls import reverse

# Create your models here.
class App(models.Model):
    name = models.CharField(("nombre aplicacion"), max_length=50, unique=True)
    logo = models.ImageField(("logo"), upload_to="images/", blank=True, null=True)
    slug = models.SlugField("slug")
    

    class Meta:
        verbose_name = ("App")
        verbose_name_plural = ("Apps")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("App_detail", kwargs={"pk": self.pk})
