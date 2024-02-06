from django.shortcuts import render, redirect, HttpResponse
import os
from cart.models import Cart
from .models import productdb
from .forms import ProductForm

# Create your views here.
def products_home(request):
    cart_obj = Cart.objects.get(user_uuid=request.user)
    productdb_var = productdb.objects.all()
    
    image_files = []
    for filename in os.listdir('static/images/banner'):
        image_files.append(filename)
    
    return render(request, 'products/products.html', {'productdb_var': productdb_var, 'images': image_files, 'carts': cart_obj})

def products_detail(request, pk):
    productdb_var = productdb.objects.get(product_uuid=pk)
    return render(request, 'products/productsdetail.html',{'single_product': productdb_var})

def add_products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                # Save the form data and redirect
                # pass
                form.save()
                return redirect('products')
        else:
            form = ProductForm()
            return render(request,'products/addproducts.html', {'form': form})
    else:
        return HttpResponse('Not Admin')

def edit_products(request, product_uuid):
    if request.user.is_superuser:
        productdb_var = productdb.objects.get(product_uuid=product_uuid)
        
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=productdb_var)
            if form.is_valid():
                form.save()
                return redirect('products')
        else:
            form = ProductForm(instance=productdb_var)
        
        return render(request, 'products/editproducts.html',{'form':form})
    else:
        return HttpResponse('Not Admin')

def delete_products(request, product_uuid):
    if request.user.is_superuser:
        productdb_var = productdb.objects.get(product_uuid=product_uuid)
        productdb_var.delete()
        return redirect('products')
    else:
        return HttpResponse('Not Admin')
    

        