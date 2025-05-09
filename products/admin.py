from django.contrib import admin
from .models import Product, Category, Size, Color



# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)