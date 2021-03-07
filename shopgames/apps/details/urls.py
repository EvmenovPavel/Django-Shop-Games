from django.urls import path
from .views import *

urlpatterns = [
    path("details/<slug:slug>", DetailsView.as_view(), name="details"),
]
