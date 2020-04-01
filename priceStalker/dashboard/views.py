import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from dashboard.forms import ProductsForm, NotificationsForm
from dashboard.classes import Form
from dashboard.models import Products, Bookmarks, Scrapers, Prices
from dashboard.scrapers.scraper import Scraper


# Create your views here.


def dashboard(request):
    productsForm = ProductsForm()
    notificationsForm = NotificationsForm()
    products = Products.objects.all().order_by('-id')[:5]
    bookmarks = Bookmarks.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {'formset': productsForm,
                                          'formset2': NotificationsForm,
                                          'products': products,
                                          'bookmarks': bookmarks})


def subscribe(request):
    if request.method == 'POST':
        notificationsForm = NotificationsForm(request.POST)
        if notificationsForm.is_valid():
            notificationsForm.save()
            url = reverse('dashboard')
        else:
            url = reverse('error')
    else:
        url = reverse('error')

    return HttpResponseRedirect(url)


def stalk(request):
    # request from fetch results in not valid form
    if request.method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        body = json.loads(bodyUnicode)
        productsForm = ProductsForm(body)
        if productsForm.is_valid():
            product = productsForm.save()
            mainUrlList = body['url'].split('/', 3)
            domain = mainUrlList[0] + '//' + mainUrlList[2] + '/'
            scraperRecord = Scrapers.objects.get(website_url=domain)
            if scraperRecord:
                scraperHandler = Scraper(body['url'])
                priceScraped = scraperHandler.getProductPrice(
                    scraperRecord.price_element_selector)
                notAvailable = 1 if priceScraped == 0 else 0
                price = Prices(product=product, price=priceScraped,
                               not_available=notAvailable)
                price.save()
                imgSrcScraped = scraperHandler.getProductImageSrc(
                    scraperRecord.image_element_selector)
                product = Products.objects.get(id=product.id)
                product.image_url = imgSrcScraped
                product.save()
            jsonResponse = JsonResponse(body)
        else:
            jsonResponse = JsonResponse({})
    else:
        jsonResponse = JsonResponse({})

    return jsonResponse


def bookmark(request):
    if request.method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        body = json.loads(bodyUnicode)
        bookmarkState = body['bookmark']
        productId = body['product']
        product = Products.objects.get(id=productId)
        bookmark = Bookmarks.objects.filter(product=product)
        if bookmark.exists():
            bookmark.update(state=bookmarkState)
        else:
            bookmark = Bookmarks(product=product, state=bookmarkState)
            bookmark.save()

        return JsonResponse({'product': productId})


def error(request):
    return render(request, 'error.html')
