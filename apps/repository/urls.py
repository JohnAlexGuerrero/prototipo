from django.urls import path

from repository.views import SoftwareCreateView

urlpatterns = [
    path('new/', SoftwareCreateView.as_view(), name='repository_new'),
]
