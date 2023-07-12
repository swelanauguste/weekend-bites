from django.urls import path

from .views import OrderDetailView, OrderListView, ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("order/", OrderListView.as_view(), name="user-order-list"),
    path("product/detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("order/detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
