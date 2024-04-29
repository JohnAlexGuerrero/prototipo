from django.urls import path

from repository.views import (
    SoftwareCreateView, SoftwareDetailView,
    CategoryCreateView, CategoryLicenseUpdateView,
    DescriptionUpdateView
)

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    
    path('<slug:slug>/', SoftwareDetailView.as_view(), name='repository'),
    path('<slug:slug>/description/', DescriptionUpdateView.as_view(), name='description'),
    path('<slug:slug>/categorization/', CategoryCreateView.as_view(), name='categorization'),
    path('<slug:slug>/c/license/', CategoryLicenseUpdateView.as_view(), name='category_license'),
    
    # path('<slug:slug>/categoria/', CategoryCreateView.as_view(), name='categorization'),
]
