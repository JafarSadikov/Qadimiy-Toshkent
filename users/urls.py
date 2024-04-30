from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views.auth import MyTokenObtainPairView, RegisterView



urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
