from django.urls import path
from . import views

urlpatterns = [
    path('api/category/<slug:category_slug>/', views.products_by_category_json, name='products_by_category_json'),
    path('api/product/<slug:slug>/', views.product_detail_json, name='product_detail_json'),
    

]
