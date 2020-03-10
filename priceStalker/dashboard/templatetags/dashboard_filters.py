from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='get_bookmark_src')
def get_bookmark_src(product):
    if product.bookmarked_product.all().first():
    	bookmarkState = product.bookmarked_product.all().first().state
    else:
    	bookmarkState = 0

    bookmarkSrc = settings.STATIC_URL + 'icons/' + \
        'bookmarked.svg' if bookmarkState else settings.STATIC_URL + 'icons/' + \
        'bookmark.svg'
    return bookmarkSrc
