from django.urls import path
from .views import *

urlpatterns = [
    path("mycart", MyCartView.as_view(), name="mycart"),
]
