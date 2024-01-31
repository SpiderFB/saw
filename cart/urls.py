from django.urls import path, re_path
from .import views

urlpatterns = [
    path('cart/', views.cart_home, name='cart'),
    path('addtocart/<uuid:product_uuid>/', views.addtocart, name=''),
    path('removefromcart/<uuid:product_uuid>/', views.removefromcart, name=''),
    
]