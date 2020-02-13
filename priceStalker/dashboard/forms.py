from django.forms import ModelForm
from django.forms import ModelForm
from dashboard.models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'url', ]
