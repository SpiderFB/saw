from django.contrib import admin

# Register your models here.
from .models import Checkout, CheckoutItem

admin.site.register(Checkout)
admin.site.register(CheckoutItem)
