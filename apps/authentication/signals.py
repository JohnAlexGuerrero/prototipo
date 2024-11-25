from authentication.models import Profile
from django.db.models.signals import post_save
from django.utils.text import slugify
# from django.contrib.auth.models import User
from django.dispatch import receiver

