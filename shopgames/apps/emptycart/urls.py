from django.urls import path
from .views import *

urlpatterns = [
    # path("empty-cart", EmptyCartView.as_view(), name="emptycart"),
    path("empty-cart", EmptyCartView.as_view(), name="emptycart"),
]
