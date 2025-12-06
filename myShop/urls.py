from django.urls import path
from .views import category_list, products_by_category

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/products/', products_by_category, name='products_by_category'),
]