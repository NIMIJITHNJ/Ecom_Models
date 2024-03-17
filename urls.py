
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home' ),
    path('products/',views.product_list, name='product_list'),
    path('products1/',views.product_list1, name='product_list1'),
]