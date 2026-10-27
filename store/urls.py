from django.urls import path
from .views import (
    ProductListView,
    CategoryProductsView,
    DiscountProductsView,
    ProductDetailView,
    ProductCreateView,
    update_product,
    delete_product,
    ShopView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('discounts/', DiscountProductsView.as_view(), name='discount_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/update/', update_product, name='update_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
]