from django.urls import path, re_path
from .import views

urlpatterns = [
    path('checkout/', views.checkout_home, name='checkout'),
    path('verify/', views.checkout_verify, name='checkoutsuccess'),
]