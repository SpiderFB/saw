from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from cart.models import Cart, CartItem
from products.models import productdb
from .models import Checkout, CheckoutItem
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt

# from checkout import models


def checkout_home(request):
    user = request.user

    # Check if the user has a cart
    try:
        cart_obj = Cart.objects.get(user_uuid=user)
    except Cart.DoesNotExist:
        # Redirect or handle the case where the user doesn't have a cart
        return HttpResponse("No Cart")


    print(Cart.total_value)
    if cart_obj.total_value  == 0 or cart_obj.num_products == 0:
        return HttpResponse("Add items to the cart plese")
    else:

        # Create a new checkout for the user
        checkout = Checkout.objects.create(user_uuid=user)

        # Copy cart items to checkout items
        for cart_item in cart_obj.cartitem_set.all():
            CheckoutItem.objects.create(
                checkout=checkout,
                product=cart_item.product,
                quantity=cart_item.quantity
            )

        # Update checkout total price and number of products
        checkout.total_price = cart_obj.total_value
        checkout.num_products = cart_obj.num_products
        checkout.save()
        
        
        
        amount = int(cart_obj.total_value  *100)   # Convert to the smallest denomination (the cent)
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_xNQuno8jmVzdoC', 'YKbGMXk0avmaRSVICO6zINWZ'))
        payment = client.order.create({'amount': amount, 'currency':  order_currency})


        # Clear the users cart after moving the contents to the checkout
        cart_obj.cartitem_set.all().delete()
        cart_obj.delete()

        # Redirect or render a success page
        return render(request, 'checkout/checkout.html', {'payment': payment})
    
@csrf_exempt   
def checkout_success(request):
    return render(request, 'checkout/success.html')