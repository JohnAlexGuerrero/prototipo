from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.http import JsonResponse

from home.models import App, Template

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app"] = App.objects.first()
        return context
    

#funcion para obtener informacion del modelo templates
def get_template_info(request):
    print(request)
    query = request.GET.get('q')
    
    infoTemplate = Template.objects.get(name=query)
    
    return JsonResponse({
        "info":[
            {
                "id": infoTemplate.id,
                "name": infoTemplate.name,
                "description": infoTemplate.description,
            }
        ]
    })
