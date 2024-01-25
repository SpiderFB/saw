from django.shortcuts import render
import os
from .models import productdb

# Create your views here.
def products_home(request):
    
    productdb_var = productdb.objects.all()
    
    image_files = []
    for filename in os.listdir('static/images/banner'):
        image_files.append(filename)
    
    return render(request, 'products/products.html', {'productdb_var': productdb_var, 'images': image_files})
