from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm  

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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form, 'title': 'პროდუქტის დამატება'})

def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'title': 'პროდუქტის რედაქტირება'})

def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'store/product_confirm_delete.html', {'product': product})