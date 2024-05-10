from django.views.generic import TemplateView

from home.models import App

class IndexView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = App.objects.first()
        return context
    
