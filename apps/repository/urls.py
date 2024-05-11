from django.urls import path

from repository.views import (
    SoftwareCreateView, SoftwareDetailView, SoftwareUpdateView, SoftwareOriginUpdateView,
    CategoryDetailView, CategoryLicenseUpdateView, CategoryGeneralUpdateView,
    SoftwareRequerimentsView, RequerimentNewView,
    DescriptionUpdateView, ArquitectureCreateView, SoftwareDeleteView
)

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    
    path('<slug:slug>/', SoftwareDetailView.as_view(), name='repository'),
    path('<slug:slug>/version/', SoftwareUpdateView.as_view(), name='version'),
    path('<slug:slug>/origin/', SoftwareOriginUpdateView.as_view(), name='type_work'),
    path('<slug:slug>/description/', DescriptionUpdateView.as_view(), name='description'),
    
    path('<slug:slug>/categorization/', CategoryDetailView.as_view(), name='categorization'),
    path('<slug:slug>/license/', CategoryLicenseUpdateView.as_view(), name='category_license'),
    path('<slug:slug>/general/', CategoryGeneralUpdateView.as_view(), name='category_general'),
    
    path('<slug:slug>/requeriments/', SoftwareRequerimentsView.as_view(), name='requeriments'),
    path('<slug:slug>/requeriment/new', RequerimentNewView.as_view(), name='requeriment_new'),
    
    path('<slug:slug>/arquitecture/', ArquitectureCreateView.as_view(), name='arquitecture_new'),
    
    path('<slug:slug>/delete/', SoftwareDeleteView.as_view(), name='delete'),
]
