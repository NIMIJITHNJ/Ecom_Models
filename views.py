from django.shortcuts import render
from .models import Product

def home(request):
    return render(request,'home.html')


def product_list(request):
    products = [
        {
            'name': 'Dodge-Grey',
            'price': 999,
            'description': 'Extra Soft Flexible Memory Foam Women Shoes for Walking, Gym Training etc',
            'image_url': 'img/shoe1.jpg'
        },
        {
            'name': 'Dodge-Blue',
            'price': 1299,
            'description': 'Extra Soft Flexible Memory Foam Women Shoes for Walking, Gym Training etc',
            'image_url': 'img/shoe2.jpg'
        },
        {
            'name': 'Dodge-Navy Blue',
            'price': 1399,
            'description': 'Extra Soft Flexible Memory Foam Women Shoes for Walking, Gym Training etc',
            'image_url': 'img/shoe3.jpg'
        },
    ]
    return render(request, 'product_list.html', {'products': products})

def product_list1(request):
    products = Product.objects.all() 
    return render(request, 'product_list1.html', {'products': products})

# Create your views here.
