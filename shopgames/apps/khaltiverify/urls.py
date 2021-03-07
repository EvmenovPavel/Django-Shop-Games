from django.urls import path
from .views import *

urlpatterns = [
    # path("khalti-verify", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("khalti-verify", KhaltiVerifyView.as_view(), name="khaltiverify"),
]
