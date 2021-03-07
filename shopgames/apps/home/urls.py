from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
