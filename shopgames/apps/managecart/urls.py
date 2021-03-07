from django.urls import path
from .views import *

urlpatterns = [
    # path("manage-cart/<int:cp_id>", ManageCartView.as_view(), name="managecart"),
    path("managecart/<int:cp_id>", ManageCartView.as_view(), name="managecart"),
]
