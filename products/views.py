from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Category

def get_products_by_category_name(name):
    category = get_object_or_404(Category, name=name)
    return Product.objects.filter(categories=category)

def popular_products(name):
    products = get_products_by_category_name("Popular")
    return JsonResponse([serialize_product(p) for p in products], safe=False)


def serialize_product(product):
    return {
        'id': product.id,
        'name': product.name,
        'price': float(product.discounted_price),
        'stock': product.stock,
        'description': product.description,
        'image': product.image.url if product.image else None,
    }