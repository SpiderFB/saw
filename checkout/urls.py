from django.urls import path, re_path
from .import views

urlpatterns = [
    path('checkout/', views.checkout_home, name='checkout'),
    path('success/', views.checkout_success, name='checkoutsuccess'),
]