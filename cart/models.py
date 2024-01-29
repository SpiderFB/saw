from uuid import uuid4
from django.db import models
from accounts.models import NewUser
from products.models import productdb

class Cart(models.Model):    
    cart_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user_uuid = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(productdb, blank=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    num_products = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cart_uuid}"