from django.forms import ModelForm
from django.forms import ModelForm
from dashboard.models import Products, Notifications


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'url',)


class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields = ('email',)
