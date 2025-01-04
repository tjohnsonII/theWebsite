from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

from django.shortcuts import render


def store_home(request):
    products = Product.objects.all()
    return render(request, 'store/store_home.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})
