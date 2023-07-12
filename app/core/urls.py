from django.urls import path

from .views import (
    OrderDetailView,
    OrderListView,
    ProductDetailView,
    ProductListView,
    order_create_view,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("orders/", OrderListView.as_view(), name="user-order-list"),
    path("order-create/<int:product_id>/", order_create_view, name="order-create"),
    path(
        "product/detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"
    ),
    path("order/detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]
