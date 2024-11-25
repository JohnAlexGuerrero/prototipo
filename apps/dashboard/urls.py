from django.urls import path

from dashboard.views import HomeView, SatisfactionView

urlpatterns = [
    path('', HomeView.as_view(), name='dashboard'),
    path('encuesta/', SatisfactionView.as_view(), name='satisfaction'),
]
