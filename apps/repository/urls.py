from django.urls import path

from repository.views import SoftwareCreateView, SoftwareDetailView
from repository.views import CategoryCreateView

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    path('<slug:slug>/', SoftwareDetailView.as_view(), name='repository'),
    path('<slug:slug>/categoria/', CategoryCreateView.as_view(), name='categorization'),
]
