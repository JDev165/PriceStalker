from django.forms import ModelForm
from django.forms import ModelForm
from dashboard.models import Products, Notifications, Bookmarks


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'url',)


class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields = ('email',)


class BookamrksForm(ModelForm):
    class Meta:
        model = Bookmarks
        fields = ()
