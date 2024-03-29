# accounts/urls.py

from django.urls import path
from .views import signup, user_login

urlpatterns = [
    path('api/signup/', signup, name='api-signup'),
    path('api/login/', user_login, name='api-login'),
]
