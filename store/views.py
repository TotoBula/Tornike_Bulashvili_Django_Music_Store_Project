from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'store/home.html', context)

def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/category_products.html', context)

def discount_products_view(request):
    products = Product.objects.filter(has_discount=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/discount_products.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)