from django.urls import path

from repository.views import (
    SoftwareCreateView, SoftwareDetailView,
    CategoryCreateView, DescriptionUpdateView
)

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    path('<slug:slug>/', SoftwareDetailView.as_view(), name='repository'),
    path('<slug:slug>/description/', DescriptionUpdateView.as_view(), name='description'),
    path('<slug:slug>/categoria/', CategoryCreateView.as_view(), name='categorization'),
]
