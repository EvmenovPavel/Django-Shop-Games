from django.urls import path
from .views import *

urlpatterns = [
    path("password-reset/<email>/<token>", PasswordResetView.as_view(), name="passwordreset"),
]
