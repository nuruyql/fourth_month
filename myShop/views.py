from django.shortcuts import render, get_object_or_404
from .models import Category


def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(
            request,
            'myShop/categories_list.html',
            {'categories': categories}
                     )

def products_by_category(request, category_id):
    if request.method == 'GET':
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()

        return render(request, 'myShop/products_list.html', {
            'category': category,
            'products': products
        })