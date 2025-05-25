from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    UserRegistrationView,
    UserProfileView,
    UserUpdateView,
    ChangePasswordView,
    logout_view,
    password_reset_request_view,
    verify_token_view,
    UsersListView
)


urlpatterns = [
    # Autenticación JWT
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_view, name='logout'),
    path('verify-token/', verify_token_view, name='verify_token'),
    
    # Gestión de usuarios
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile_update'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password-reset/', password_reset_request_view, name='password_reset_request'),
    
    # Lista de usuarios
    path('users/', UsersListView.as_view(), name='users_list'),
]