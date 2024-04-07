from django.urls import path

from repository.views import SoftwareCreateView, SoftwareDetailView

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
    path('<slug:slug_user>/<slug:slug_repo>/', SoftwareDetailView.as_view(), name='repository'),
]
