from django.urls import path
from .views import *

urlpatterns = [
    path("admin-login", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>", AdminOrderDetailView.as_view(), name="adminorderdetail"),
    path("admin-all-orders", AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change", AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),
    path("admin-product/list", AdminProductListView.as_view(), name="adminproductlist"),
    path("admin-product/add", AdminProductCreateView.as_view(), name="adminproductcreate"),
]
