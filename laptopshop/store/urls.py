from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('laptop/<int:pk>/', views.laptop_detail, name='laptop_detail'),
    path('cart/', views.view_cart, name='view_cart'),
    path('register/', views.register_view, name='register'),
    path('call-center/', views.call_center, name='call_center'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/<int:laptop_id>/', views.cart, name='cart'),
]
