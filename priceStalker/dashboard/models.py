from datetime import datetime
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=2000, blank=False)
    date_stalked = models.DateTimeField(auto_now_add=True, blank=False)

    # override the way this model is displayed in the admin side
    # without this, all we see is 'Products Object'

    def __str__(self):
        return self.name


class Prices(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='product',
                                related_query_name='product')

    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.price


class Notifications(models.Model):
    email = models.EmailField(max_length=50, blank=False)

    def __str__(self):
        return self.email


class Bookmarks(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='bookmarked_product',
                                related_query_name='bookmarked_product')

    date_bookmarked = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.product


class Keywords(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='tagged_product',
                                related_query_name='tagged_product')

    keyword = models.CharField(max_length=50, blank=False)

    date_tagged = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.product
