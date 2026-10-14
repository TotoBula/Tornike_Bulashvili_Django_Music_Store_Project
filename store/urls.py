from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<int:category_id>/', views.category_products_view, name='category_products'),
    path('discounts/', views.discount_products_view, name='discount_products'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
]