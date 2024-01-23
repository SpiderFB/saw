from django.shortcuts import render, HttpResponse
import uuid
from .models import NewUser

# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        user_uuid = uuid.uuid4()  # Generate a new UUID

        print(email, password, phone, user_uuid)
        user = NewUser(email=email, phone=phone, is_staff=False, is_superuser=False)
        user.set_password('password')
        user.save()

        return HttpResponse("Okay")
    else:
        return render(request, 'accounts/accounts.html')