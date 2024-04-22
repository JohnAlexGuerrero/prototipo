from django.urls import path

from authentication.views import (
    UserLoginView, 
    user_logout_view,
    CustomUserCreateView,
    ProfileDetailView,
    AcademicaCreateView,
    ContactUpdateView,
    CustomUserUpdateView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('register/', CustomUserCreateView.as_view(), name='signup'),
    path('<slug:slug>/info-contact/', ContactUpdateView.as_view(), name="contact"),
    path('<slug:slug>/info-personal/', CustomUserUpdateView.as_view(), name="personal"),
    # path('<slug:slug>/profile/', ProfileView.as_view(), name='profile'),
    path('<slug:slug>/info-academica/', AcademicaCreateView.as_view(), name='academica'),
    # path('<slug:slug>/edit', ProfileUpdateView.as_view(), name='profile_edit' ),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile' ),
]


