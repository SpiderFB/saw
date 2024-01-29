from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
import os
from .models import Cart
from accounts.models import NewUser
from products.models import productdb
from django.contrib.auth.decorators import login_required

# Create your views here.


def cart_home(request):
    print(request.user)
    cart_obj, created = Cart.objects.get_or_create(user_uuid=request.user, defaults={'total_value': 0, 'num_products': 0})
    if created:
        cart_obj.save()
    print(cart_obj)
    return render(request, 'cart/cart.html',{'carts': cart_obj})


@login_required
def addtocart(request, product_uuid):
    productdb_var = productdb.objects.get(product_uuid=product_uuid)
    cart_var = Cart.objects.get(user_uuid=request.user)
    print(productdb_var.product_name)
    
    cart_var.total_value += productdb_var.product_price
    cart_var.num_products += 1
    cart_var.cart_products.add(productdb_var.product_uuid)
    
    print(cart_var.total_value)
    
    cart_var.save()
    
    return redirect('products')


