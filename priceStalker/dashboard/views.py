from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from dashboard.forms import ProductsForm, NotificationsForm
from dashboard.classes import Form


# Create your views here.


def dashboard(request):
    productsForm = ProductsForm()
    notificationsForm = NotificationsForm()
    return render(request, 'index.html', {'formset': productsForm,
                                          'formset2': NotificationsForm})


def subscribe(request):
    if request.method == 'POST':
        notificationsForm = NotificationsForm(request.POST)
        if notificationsForm.is_valid():
            notificationsForm.save()
            url = reverse('dashboard')
        else:
            url = reverse('error')
        return HttpResponseRedirect(url)


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
