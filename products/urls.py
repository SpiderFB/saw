from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.products_home, name=''),
    path('products/', views.products_home, name='products'),
    re_path(r'^productsdetail/(?P<pk>[0-9a-f-]+)/$', views.products_detail, name=''), # can be sent also as UUID like in the edit_product
    path('addproducts/', views.add_products, name=''),
    path('editproducts/<uuid:product_uuid>/', views.edit_products, name=''),
    path('deleteproducts/<uuid:product_uuid>/', views.delete_products, name=''),
]