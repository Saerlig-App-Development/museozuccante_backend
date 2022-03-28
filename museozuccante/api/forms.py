from django import forms
from pagedown.widgets import AdminPagedownWidget

from api.models import Item, Company


class ItemModelForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Item
        fields = '__all__'


class CompanyModelForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Company
        fields = '__all__'
