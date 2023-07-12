from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import OrderCreateForm
from .models import Category, Order, Product


@login_required
def order_create_view(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    data = {"product": product, "user": user}
    form = OrderCreateForm(initial=data)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        user = request.user
        product = Product.objects.get(id=product_id)
        order_qty = request.POST.get("qty")
        if form.is_valid:
            form.save(commit=False)
            form.user = user
            form.save()
            messages.success(
                request, f"Your order of {order_qty}, {str(product).title()} has been submitted"
            )
            return redirect("product-list")

        # print(order_qty, user, product)

    return render(
        request, "core/order_create.html", context={"form": form, "product": product}
    )


# game = Game.objects.get(id=1) # just an example
#     data = {'id': game.id, 'position': game.position}
#     form = UserQueueForm(initial=data)
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        query = self.request.GET.get("orders")
        if query:
            return Order.objects.filter(
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
            return Product.objects.filter(is_available=True)


class ProductDetailView(DetailView):
    model = Product
