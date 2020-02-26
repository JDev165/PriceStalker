import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from dashboard.forms import ProductsForm, NotificationsForm
from dashboard.classes import Form
from dashboard.models import Products 


# Create your views here.


def dashboard(request):
    productsForm = ProductsForm()
    notificationsForm = NotificationsForm()
    products = Products.objects.all()
    return render(request, 'index.html', {'formset': productsForm,
                                          'formset2': NotificationsForm, 
                                          'products': products})


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
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        productsForm = ProductsForm(body)
        if productsForm.is_valid():
            productsForm.save()
            return JsonResponse(body)


def error(request):
    return render(request, 'error.html')


# if request.method == 'POST':
 #        productsForm = Form(ProductsForm(request.method))
 #        productRecord = productsForm.saveRecord()

 #        url = reverse('success', kwargs={'workoutID': productRecord.id})
 #        return HttpResponseRedirect(url)
 #    else:
 #        productsForm = ProductsForm()

 #    return render(request, 'manage.html', {'formset': productsForm})
 #
