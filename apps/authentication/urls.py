from django.urls import path

from authentication.views import UserLoginView, user_logout_view, CustomUserCreateView, ProfileUpdateView, ProfileDetailView, UserProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('register/', CustomUserCreateView.as_view(), name='signup'),
    path('profile/<slug:slug>/', UserProfileView.as_view(), name='profile_new'),
    path('<slug:slug>/edit', ProfileUpdateView.as_view(), name='profile_edit' ),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile' ),
]


