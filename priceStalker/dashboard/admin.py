from django.contrib import admin
from .models import Products, Prices

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('product_name', 'product_url',)


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    fields = ('product', 'price',)
