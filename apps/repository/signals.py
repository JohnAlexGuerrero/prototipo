from repository.models import Software, Category

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify

@receiver(post_save, sender=Software)
def post_save_create_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.create(software=instance, slug=instance.slug)