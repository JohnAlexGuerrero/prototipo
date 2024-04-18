from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from repository.models import Software
from authentication.models import CustomUser

from authentication.forms import UserOccupationForm

class HomeView(TemplateView):
    template_name = "dashboard/index.html"
    model = CustomUser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["repositories"] = Software.objects.filter(user=self.request.user)
        context['form'] = UserOccupationForm
        return context