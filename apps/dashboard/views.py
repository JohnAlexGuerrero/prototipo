from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

from repository.models import Software
from authentication.models import Profile
from home.models import App


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["repositories"] = Software.objects.filter(user=self.request.user)
        context['app'] = App.objects.first()
        return context
    
#view encuesta de satisfaccion de aplicativo
class SatisfactionView(TemplateView):
    template_name = "dashboard/satisfaction.html"
