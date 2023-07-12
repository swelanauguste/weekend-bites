from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "product",
            "qty",
            "user",
        )
        widgets = {"user": forms.HiddenInput(), 'product': forms.HiddenInput()}
