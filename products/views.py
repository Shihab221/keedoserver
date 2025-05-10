from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category

def products_by_category_json(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()

    data = []
    for product in products:
        data.append({
            'name': product.name,
            'slug': product.slug,
            'image': product.image.url if product.image else '',
            'description': product.description,
            'regular_price': str(product.regular_price),
            'discounted_price': str(product.discounted_price),
            'stock': product.stock,
            'rating': str(product.rating),
            'sizes': [size.name for size in product.sizes.all()],
            'colors': [color.name for color in product.colors.all()],
        })

    return JsonResponse({'category': category.name, 'products': data})


def product_detail_json(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    data = {
        'name': product.name,
        'slug': product.slug,
        'image': product.image.url if product.image else '',
        'description': product.description,
        'detailed_description': product.detailed_description,
        'regular_price': str(product.regular_price),
        'discounted_price': str(product.discounted_price),
        'stock': product.stock,
        'rating': str(product.rating),
        'categories': [cat.name for cat in product.categories.all()],
        'sizes': [size.name for size in product.sizes.all()],
        'colors': [color.name for color in product.colors.all()],
    }

    return JsonResponse(data)
