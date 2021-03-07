from django.urls import path
from .views import *

urlpatterns = [
    path("profile/order-<int:pk>", OrderDetailView.as_view(), name="derdetail"),
]
