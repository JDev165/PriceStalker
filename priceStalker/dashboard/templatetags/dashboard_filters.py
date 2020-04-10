from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='get_bookmark_src')
def get_bookmark_src(product):
    bookmarkState = product.bookmarked_product.all().first()
    if not bookmarkState:
        bookmarkState = 0
    else:
        bookmarkState = bookmarkState.state

    bookmarkSrc = settings.STATIC_URL + 'icons/' + \
        'bookmarked.svg' if bookmarkState else settings.STATIC_URL + 'icons/' + \
        'bookmark.svg'
    return bookmarkSrc


@register.filter(name='get_product_price')
def get_product_price(product):
    productPrice = product.product_price.all().order_by('-id').first()
    if not productPrice:
        productPrice = 0
    else:
        productPrice = productPrice.price

    productPriceWithSymbol = '$' + str(productPrice)
    return productPriceWithSymbol


@register.filter(name='set_last_element_class')
def set_last_element_class(last):
    lastClass = "last-product" if last else ""
    return lastClass
