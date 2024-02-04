from uuid import uuid4
from django.db import models
from accounts.models import NewUser
from products.models import productdb

# Create your models here.
class Checkout(models.Model):
    checkout_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user_uuid = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    total_price =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    num_products = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.checkout_uuid}"
    
class CheckoutItem(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    product = models.ForeignKey(productdb, on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"