from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import ProductsForm, NotificationsForm
from dashboard.classes import Form

# Create your views here.


def dashboard(request):
    productsForm = ProductsForm()
    notificationsForm = NotificationsForm()
    return render(request, 'index.html', {'formset': productsForm, 
    									  'formset2': NotificationsForm})

 # if request.method == 'POST':
 #        productsForm = Form(ProductsForm(request.method))
 #        productRecord = productsForm.saveRecord()

 #        url = reverse('success', kwargs={'workoutID': productRecord.id})
 #        return HttpResponseRedirect(url)
 #    else:
 #        productsForm = ProductsForm()

 #    return render(request, 'manage.html', {'formset': productsForm})
 #
