from django.urls import path
from .import views

urlpatterns = [
    path('accounts/', views.accounts_home, name=''),
    path('signup/', views.user_signup, name=''),
    path('signin/', views.user_signin, name=''),
    path('signout/', views.user_signout, name=''),
]