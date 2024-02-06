from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import resolve
from cart.models import Cart, CartItem
from products.models import productdb
from .models import Checkout, CheckoutItem
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os


# from checkout import models

@login_required
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
                quantity=cart_item.quantity,
            )

        # Update checkout total price and number of products
        checkout.total_price = cart_obj.total_value
        checkout.num_products = cart_obj.num_products
        checkout.save()
        
        amount = int(cart_obj.total_value  *100)   # Convert to the smallest denomination (the cent)
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_YkLyjJgCoPN0hj", "IfqCzq284jhWtBNr61gEayCZ"))
        payment = client.order.create({'amount': amount, 'currency':  order_currency})
        
        return render(request, 'checkout/checkout.html', {'payment': payment})
    
      
@csrf_exempt
def checkout_verify(request):
    
    # cart_obj = Cart.objects.get(user_uuid=request.user)
    
    if request.method == 'POST':
        
        #When payment success
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        
        #When payment fails
        razorpay_error_code = request.POST.get('error[code]')
        razorpay_error_description = request.POST.get('error[description]')
        razorpay_error_source = request.POST.get('error[source]')
        razorpay_error_step = request.POST.get('error[step]')
        razorpay_error_reason = request.POST.get('error[reason]')
        razorpay_error_metadata = request.POST.get('error[metadata]')
        
        if razorpay_error_code:
            print(razorpay_error_description)
            print(razorpay_error_source)
            print(razorpay_error_step)
            print(razorpay_error_reason)
            print(razorpay_error_metadata)
            # return HttpResponse("New issue")
            return redirect('checkout_failure', razorpay_error_code, razorpay_error_description)
        
        # Verify the signature is valid or not using the Razorpay API
        client = razorpay.Client(auth=("rzp_test_YkLyjJgCoPN0hj", "IfqCzq284jhWtBNr61gEayCZ"))
        # payment = client.payment.fetch(razorpay_payment_id)
        if client.utility.verify_payment_signature({
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        'razorpay_signature': razorpay_signature
        # 'razorpay_signature': 1
        }):
            
            return redirect('checkout_success', razorpay_order_id, razorpay_payment_id)
        # Payment signature is invalid
        else:
            return HttpResponse("Invalid Signature")
    else:
        return HttpResponse("Payment issue")
    
def checkout_success(request, razorpay_order_id, razorpay_payment_id):
    
    # Update your application's state based on the payment status
            # ...
            # Clear the users cart after moving the contents to the checkout
    cart_obj = Cart.objects.get(user_uuid=request.user)  
    cart_obj.cartitem_set.all().delete()
    cart_obj.delete()     
    
    
    
    
    
    checkout_obj = Checkout.objects.filter(user_uuid=request.user).last()
    # Update the Checkout object with the razorpay_order_id
    checkout_obj.razorpay_order_id = razorpay_order_id
    checkout_obj.razorpay_payment_id = razorpay_payment_id
    checkout_obj.save()
    
    
     
     
     
    
    
    context = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': razorpay_payment_id,
        # 'saw_order_id' : checkout_obj.checkout_uuid,
        
        }
    return render(request, 'checkout/success.html', context)

def checkout_failure(request, razorpay_error_code, razorpay_error_description):
    
    checkout_obj = Checkout.objects.filter(user_uuid=request.user).last()
    checkout_obj.delete()

    context = {
        'razorpay_error_code': razorpay_error_code,
        'razorpay_error_description': razorpay_error_description,
        }
    return render (request, 'checkout/failure.html', context)