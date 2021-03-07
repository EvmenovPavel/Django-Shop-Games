from django.urls import path
from .views import *

urlpatterns = [
    path("add-to-cart-<int:pro_id>", AddToCartView.as_view(), name="addtocart"),
]
