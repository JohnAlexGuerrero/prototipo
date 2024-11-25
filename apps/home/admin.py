from django.contrib import admin

from home.models import App, Template

# Register your models here.
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass

