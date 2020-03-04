from django.contrib import admin
from .models import Products, Prices, Notifications, Bookmarks, Keywords

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'url',)


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    fields = ('product', 'price',)


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    fields = ('email',)


@admin.register(Bookmarks)
class BookmarksAdmin(admin.ModelAdmin):
    fields = ('product',)


@admin.register(Keywords)
class BookmarksAdmin(admin.ModelAdmin):
    fields = ('product',)
