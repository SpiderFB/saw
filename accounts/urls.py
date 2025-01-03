from django.urls import path
from .import views

urlpatterns = [
    path('accounts/', views.accounts_home, name='accounts'),
    path('signup/', views.user_signup, name=''),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_signout, name=''),
    path('profile/', views.user_profile, name=''),
]