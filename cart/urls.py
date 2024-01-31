from django.urls import path, re_path
from .import views

urlpatterns = [
    path('cart/', views.cart_home, name='cart'),
    path('addtocart/<uuid:product_uuid>/', views.addtocart, name=''),
    path('reducefromcart/<uuid:product_uuid>/', views.reducefromcart, name=''),
    path('deletefromcart/<uuid:product_uuid>/', views.deletefromcart, name=''),
    
]