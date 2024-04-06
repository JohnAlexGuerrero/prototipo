from authentication.models import Profile
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from authentication.models import CustomUser
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def post_save_create_profile(sender, instance, created, **kwargs):
  print(sender)
  print(instance)
  print(created)
  if created:
    Profile.objects.create(user=instance)