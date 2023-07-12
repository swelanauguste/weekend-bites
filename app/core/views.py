from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Order, Product


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        query = self.request.GET.get("orders")
        if query:
            return Product.objects.filter(
                Q(product__name__icontains=query),
                user=self.request.user,
            ).distinct()
        else:
            return Order.objects.filter(user=self.request.user)


class OrderDetailView(DetailView):
    model = Order


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get("products")
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) | Q(tags__category__icontains=query),
                is_available=True,
            ).distinct()
        else:
            return Product.objects.all(is_available=True)


class ProductDetailView(DetailView):
    model = Product
