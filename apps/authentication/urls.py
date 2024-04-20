from django.urls import path

from authentication.views import (
    UserLoginView, 
    user_logout_view,
    CustomUserCreateView,
    ProfileDetailView,
    AcademicaCreateView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('register/', CustomUserCreateView.as_view(), name='signup'),
    # path('<slug:slug>/profile/', ProfileView.as_view(), name='profile'),
    path('<slug:slug>/info-academica/', AcademicaCreateView.as_view(), name='academica'),
    # path('<slug:slug>/edit', ProfileUpdateView.as_view(), name='profile_edit' ),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile' ),
]


