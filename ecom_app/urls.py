
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home'),
    path('fitness', views.fitness, name='fitness'),
    path('barbells', views.barbells, name='barbells'),
    path('dumbbells', views.dumbbells, name='dumbbells'),
    path('cart', views.cart, name='cart'),
    path('product/', views.product, name="pics2"),
]