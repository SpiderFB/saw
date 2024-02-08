from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
import os
from cart.models import Cart
from .models import productdb
from .forms import ProductForm


# Create your views here.
def products_home(request):
    
    productdb_var = productdb.objects.all()
    
    image_files = []
    for filename in os.listdir('static/images/banner'):
        image_files.append(filename)
        
    if request.user.is_authenticated:
        cart_obj, created = Cart.objects.get_or_create(user_uuid=request.user)    
        context = {
            'productdb_var': productdb_var,
            'images': image_files,
            'carts': cart_obj,
        }
        return render(request, 'products/products.html',context)
    else:
        return render(request, 'products/products.html', {'productdb_var': productdb_var, 'images': image_files})

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
    
def fav(request, product_uuid):
    if request.user.is_authenticated:
        product = get_object_or_404(productdb, product_uuid=product_uuid)
        if product in request.user.fav_product.all():
            # Product is already in fav_product set, so remove it
            request.user.fav_product.remove(product)
            request.user.save()
            return HttpResponse("removed")
        else:
            # Product is not in fav_product set, so add it
            request.user.fav_product.add(product)
            request.user.save()
            return HttpResponse("added")
    else:
        return redirect('accounts')
    

        