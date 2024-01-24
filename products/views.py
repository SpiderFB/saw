from django.shortcuts import render
import os

# Create your views here.
def products_home(request):
    
    image_files = []
    for filename in os.listdir('static/images/banner'):
        # if filename.endswith('.jpg') or filename.endswith('.png'):
        image_files.append(filename)
    
    return render(request, 'products/products.html', {'images': image_files})
