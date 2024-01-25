from django.contrib import admin

# Register your models here.
from .models import productdb, category

admin.site.register(productdb)
admin.site.register(category)