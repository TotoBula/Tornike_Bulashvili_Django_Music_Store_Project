from .models import Product, Category

def store_context(request):
    return {
        'categories': Category.objects.all(),
        'product_list': Product.objects.select_related('category').all(),
        'site_name': 'My Store',
    }