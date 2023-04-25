from django.shortcuts import render, HttpResponse
from products.models import ProductCategory, Product
# Create your views here.


def index(request):
    content = {
        'title': 'Store',
        'isPromotion': False
    }
    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, "products/products.html", content)
