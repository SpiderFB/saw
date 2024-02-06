from django.urls import path, re_path
from .import views

urlpatterns = [
    path('checkout/', views.checkout_home, name='checkout'),
    path('verify/', views.checkout_verify, name=''),
    path('checkout_success/<str:razorpay_order_id>/<str:razorpay_payment_id>/', views.checkout_success, name='checkout_success'),
    path('checkout_failure/<str:razorpay_error_code>/<str:razorpay_error_description>/', views.checkout_failure, name='checkout_failure'),
]