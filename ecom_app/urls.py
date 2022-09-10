
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fitness', views.fitness, name='fitness'),
    path('barbells', views.barbells, name='barbells'),
    path('dumbbells', views.dumbbells, name='dumbbells'),
    path('cart', views.cart, name='cart'),
    path('product/', views.product, name="pics2"),
]