from django.contrib import admin

from home.models import App

# Register your models here.
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass

