from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Product
from .forms import ProductForm  

# 1. მთავარი გვერდი (ListView)
class ProductListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        return context


# 2. კატეგორიის პროდუქტები (ListView ფილტრაციით)
class CategoryProductsView(ListView):
    model = Product
    template_name = 'store/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Product.objects.select_related('category').filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        return context


# 3. ფასდაკლებული პროდუქტები (ListView ფილტრაციით)
class DiscountProductsView(ListView):
    model = Product
    template_name = 'store/discount_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category').filter(has_discount=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        return context


# 4. პროდუქტის დეტალური გვერდი (DetailView)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Product.objects.select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        return context


# 5. პროდუქტის დამატება (CreateView)
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'პროდუქტის დამატება'
        return context


# 6. UPDATE და DELETE
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
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

# 7. შოპის/ყველა პროდუქტის გვერდი (ListView)
class ShopView(ListView):
    model = Product
    template_name = 'store/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(product_count=Count('products'))
        return context