from django.urls import path
from .views import *

urlpatterns = [
    path("forgot-password", PasswordForgotView.as_view(), name="passworforgot"),
]
