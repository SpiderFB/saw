from django.shortcuts import render, HttpResponse
import uuid
from .models import NewUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            return HttpResponse("Signin Success")
        else:
            return render(request, 'accounts/signin.html')
    else:
        return render(request, 'accounts/signin.html')

@login_required 
def user_signout(request):
    logout(request)
    return render(request, 'accounts/accounts.html')