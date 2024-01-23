from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']

        print(email, password, phone)

        return HttpResponse("Okay")
    else:
        return render(request, 'accounts/accounts.html')

