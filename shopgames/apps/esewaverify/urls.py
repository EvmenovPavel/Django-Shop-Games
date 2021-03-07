from django.urls import path
from .views import *

urlpatterns = [
    path("esewa-verify", EsewaVerifyView.as_view(), name="esewaverify"),
]
