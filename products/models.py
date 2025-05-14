from django.utils.text import slugify
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default=1)
    slug = models.SlugField(unique=True, blank = True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=10)  # e.g. S, M, L, XL, 32, 42

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30)  # e.g. Red, Blue
    hex_code = models.CharField(max_length=7, blank=True)  # optional

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    description = models.CharField(max_length=255)
    detailed_description = CKEditor5Field("Description", config_name="extends", blank=True, null=True)
    regular_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=4.5)
    sizes = models.ManyToManyField(Size, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name