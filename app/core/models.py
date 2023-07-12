from django.db import models
from django.urls import reverse
from users.models import User


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Category)
    image = models.ImageField(null=True, blank=True, upload_to="product/img")
    desc = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["-price"]

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders"
    )
    qty = models.PositiveIntegerField("Quantity", default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_orders")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("order-detail", kwargs={"pk": self.pk})

    def get_total_price(self):
        return self.qty * self.product.price

    def __str__(self):
        return f"{self.user.username}'s order of {self.product.name}"
