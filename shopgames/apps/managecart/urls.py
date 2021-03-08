from django.urls import path
from .views import *

urlpatterns = [
    path("managecart/<int:cp_id>", ManageCartView.as_view(), name="managecart"),
]
