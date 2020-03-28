from datetime import datetime
from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50, blank=False)
    url = models.URLField(max_length=2000, blank=False)
    # Remove blank default when we start populating this
    image_url = models.URLField(max_length=2000, blank=False, default='blank')
    date_stalked = models.DateTimeField(auto_now_add=True, blank=False)

    # override the way this model is displayed in the admin side
    # without this, all we see is 'Products Object'

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Prices(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='product_price',
                                related_query_name='product_price')

    price = models.DecimalField(max_digits=6, decimal_places=2)

    not_available = models.BooleanField(default=0, blank=False)

    class Meta:
        verbose_name_plural = 'Prices'

    def __str__(self):
        return str(self.price)


class Notifications(models.Model):
    email = models.EmailField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return self.email


class Bookmarks(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,
                                related_name='bookmarked_product',
                                related_query_name='bookmarked_product')

    state = models.BooleanField(default=0, blank=False)

    date_bookmarked = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        verbose_name_plural = 'Bookmarks'

    def __str__(self):
        return str(self.state)


class Scrapers(models.Model):

    website_url = models.CharField(max_length=500, blank=False)

    price_element_selector = models.CharField(max_length=500, blank=False)

    image_element_selector = models.CharField(max_length=500, blank=False)

    class Meta:
        verbose_name_plural = 'Scrapers'

    def __str__(self):
        return self.website_url
