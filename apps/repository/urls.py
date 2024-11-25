from django.urls import path

from repository.views import (
    SoftwareCreateView, SoftwareDetailView, SoftwareVersionView, SoftwareOriginUpdateView,
    CategoryDetailView, CategoryLicenseUpdateView, SoftwarePublicView,
    SoftwareRequerimentsView, RequerimentNewView, RequerimentUpdateView,
    DescriptionUpdateView, SoftwareDeleteView, SoftwareLogoView, AuthorListView,
    PlatformView, CodeSourceView, AuthorView, UserManualView, CopyrightView, InstallationUpdateView,
    delete_author
)
from home.views import get_template_info

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    
    path('<slug:slug>/', SoftwareDetailView.as_view(), name='repository'),
    
    path('<slug:slug>/logo/', SoftwareLogoView.as_view(), name='logo'),
    path('<slug:slug>/version/', SoftwareVersionView.as_view(), name='version'),
    path('<slug:slug>/origin/', SoftwareOriginUpdateView.as_view(), name='type_work'),
    path('<slug:slug>/license/', CategoryLicenseUpdateView.as_view(), name='category_license'),
    path('<slug:slug>/public/', SoftwarePublicView.as_view(), name='public'),
    path('<slug:slug>/plataforma-tecnologica/', PlatformView.as_view(), name='platform'),
    path('<slug:slug>/requerimiento/<int:pk>/hardware/', InstallationUpdateView.as_view(), name='hardware'),
    path('<slug:slug>/autor/new', AuthorView.as_view(), name='authors'),
    path('<slug:slug>/autores/', AuthorListView.as_view(), name='detail_author'),
    path('<slug:slug>/autor/eliminar/<int:pk>', delete_author, name='delete_author'),
    path('<slug:slug>/description/', DescriptionUpdateView.as_view(), name='description'),
    path('<slug:slug>/requeriment/new', RequerimentNewView.as_view(), name='requeriment_new'),
    
    path('<slug:slug>/codigo-fuente/', CodeSourceView.as_view(), name='code_surce'),
    
    path('<slug:slug>/requeriments/', SoftwareRequerimentsView.as_view(), name='requeriments'),
    path('<slug:software_slug>/requeriments/edit', RequerimentUpdateView.as_view(), name='requeriment_edit'),
    
    path('<slug:slug>/categorization/', CategoryDetailView.as_view(), name='categorization'),
    
    path('<slug:slug>/delete/', SoftwareDeleteView.as_view(), name='delete'),
    
    path('<slug:slug>/generate/manual-usuario/', UserManualView.as_view(), name='user-manual'),
    
    path('<slug:slug>/copyright/', CopyrightView.as_view(), name='copyright'),
    
    path('info/template/', get_template_info, name='info-template'),
    
]
