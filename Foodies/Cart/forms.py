from django import forms
from django.forms import widgets


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField()
    override = forms.BooleanField(required=False,
    initial=False, widget=forms.HiddenInput(attrs={'class': 'rounded_list'})
    )
    quantity.widget.attrs.update({'class': 'form-control'})

