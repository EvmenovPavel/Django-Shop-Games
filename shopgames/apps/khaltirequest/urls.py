from django.urls import path
from .views import *

urlpatterns = [
    # path("khalti-request", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-request", KhaltiRequestView.as_view(), name="khaltirequest"),
]
