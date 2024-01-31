from uuid import uuid4
from django.db import models
from accounts.models import NewUser
from products.models import productdb

class Cart(models.Model):
    cart_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user_uuid = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    num_products = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cart_uuid}"
     
    def save(self, *args, **kwargs):
        # Calculate total_value based on CartItem quantities and product prices
        self.total_value = sum(item.quantity * item.product.product_price for item in self.cartitem_set.all())
        
        # Calculate num_products as the sum of quantities
        self.num_products = sum(item.quantity for item in self.cartitem_set.all())
        
        super().save(*args, **kwargs)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(productdb, on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"