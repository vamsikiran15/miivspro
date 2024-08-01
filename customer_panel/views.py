# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Order, OrderItem

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'store/product_detail.html', {'product': product})

# def cart(request):
#     return render(request, 'store/cart.html')

# def checkout(request):
#     return render(request, 'store/checkout.html')
