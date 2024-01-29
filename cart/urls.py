from django.urls import path, re_path
from .import views

urlpatterns = [
    path('cart/', views.cart_home, name=''),
    path('addtocart/<uuid:product_uuid>/', views.addtocart, name=''),
    
]