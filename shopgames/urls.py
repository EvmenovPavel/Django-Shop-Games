from django.contrib import admin
from django.urls import path, include

handler400 = "error.views.bad_request"
handler403 = "error.views.permission_denied"
handler404 = "error.views.page_not_found"
handler500 = "error.views.server_error"

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    path("", include("shopgames.apps.urls")),
]
