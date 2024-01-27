from django import forms
from .models import productdb

class ProductForm(forms.ModelForm):
    class Meta:
        model = productdb
        fields = ['product_name', 'product_description', 'product_category', 'product_price', 'product_quantity', 'product_image', 'product_brand']

    # Add custom validation for product_price and product_quantity
    def clean(self):
        cleaned_data = super().clean()
        product_price = cleaned_data.get("product_price")
        product_quantity = cleaned_data.get("product_quantity")

        if product_price <= 0:
            self.add_error('product_price', 'Product price must be greater than zero.')

        if product_quantity <= 0:
            self.add_error('product_quantity', 'Product quantity must be greater than zero.')