from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Cart, CartItem
from products.models import productdb
from django.contrib.auth.decorators import login_required

from cart import models

# Create your views here.


def cart_home(request):
    print(request.user)
    cart_obj, created = Cart.objects.get_or_create(user_uuid=request.user, defaults={'total_value': 0, 'num_products': 0})
    if created:
        cart_obj.save()
    print(cart_obj)
    
    
    cart_items = cart_obj.cartitem_set.all()
    
    return render(request, 'cart/cart.html',{'carts': cart_obj, 'cart_items': cart_items})


@login_required
def addtocart(request, product_uuid):
    cart, created = Cart.objects.get_or_create(user_uuid=request.user)
    product = get_object_or_404(productdb, product_uuid=product_uuid)
    
    # Checking if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    print(cart_item)

    # If the item is already in the cart, update the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Update the total value and quantity of the cart
    cart.save()
    
    return redirect('cart')

def removefromcart(request, product_uuid):

    cart= Cart.objects.get(user_uuid=request.user)
    product = get_object_or_404(productdb, product_uuid=product_uuid)
    cart_item= CartItem.objects.get(cart=cart, product=product)
    cart_item.quantity -= 1
    cart_item.save()
    cart.save()
    
    return redirect('cart')
