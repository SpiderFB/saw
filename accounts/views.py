from django.shortcuts import render, HttpResponse, redirect
import uuid
from .models import NewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from checkout.models import Checkout

# Create your views here.
def accounts_home(request):
    return render(request, 'accounts/accounts.html')

def user_signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        user_uuid = uuid.uuid4()  # Generate a new UUID

        if NewUser.objects.filter(email=email).exists():
            return HttpResponse("Error: A user with this email already exists.")

        print(email, password, phone, user_uuid)
        user = NewUser(email=email, phone=phone, is_staff=False, is_superuser=False)
        user.set_password(password)
        user.save()

        return HttpResponse("SignedUP succesfully")
    else:
        return render(request, 'accounts/signup.html')
    
    
def user_signin(request):
    if request.method == "POST":
        email = request.POST['email123']
        password = request.POST['password123']
        # print(username, password)
        user = authenticate(request, email=email, password=password)
        print (user)
        if user is not None:
            login(request, user)
            # return HttpResponse("Signin Success")
            return redirect('products')
        else:
            return render(request, 'accounts/signin.html')
    else:
        return render(request, 'accounts/signin.html')

@login_required 
def user_signout(request):
    logout(request)
    return render(request, 'accounts/accounts.html')

def user_profile(request):
    user_obj = NewUser.objects.get(id=request.user.id)
    checkout_obj = Checkout.objects.filter(razorpay_order_id__isnull=False, user_uuid = request.user)
    print("Chekout obj returns" ,checkout_obj)
    
    return render(request,'accounts\profile.html',{'user_obj': user_obj, 'checkout_obj': checkout_obj} )  

# # @csrf_exempt
# @login_required
# def update_profile(request):
#     if request.method=='POST':
#         id=request.user.id
#         name=request.POST["name"]
#         phone=request.POST["phone"]
#         address=request.POST["address"]
        
#         try:
#             UserProfile.objects.filter(id=id).update(Name=name, PhoneNo=phone, Address=address)
#             data="Data Updated"
#         except Exception as e:
#             data=str(e)
            
#         t=loader.get_template('accounts/profile.html')
#         c=Context({'data':UserProfile.objects.get(id=id),'message':data})
#         html_content=t.render(c)
#         return HttpResponse(html_content)    
#     else:
#         return HttpResponse("Method Not Allowed")