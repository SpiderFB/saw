from django.urls import path
from .import views
from django.urls import re_path

urlpatterns = [
    path('', views.products_home, name=''),
    path('products/', views.products_home, name=''),
    # path('productsdetail/<int:pk>/', views.products_detail, name=''),
    re_path(r'^productsdetail/(?P<pk>[0-9a-f-]+)/$', views.products_detail, name=''), # Update the pattern
]