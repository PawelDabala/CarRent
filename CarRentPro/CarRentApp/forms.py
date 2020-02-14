from django import forms
from .models import Address, Maciek


# class AddressForm(forms.Form):
#     """AddressForm definition."""

#     # TODO: Define form fields here
#     street = forms.CharField(max_length=50)
#     bulding = forms.CharField(max_length=50)
#     flat = forms.CharField(max_length=50)
#     post_code = forms.DecimalField()
#     city = forms.CharField(max_length=50)


class MaciekForm(forms.Form):
    """Maciek definition."""

    # TODO: Define form fields here
    name = forms.CharField(max_length=50)


class AddressForm(forms.Form):
    """AddressForm definition."""

    # TODO: Define form fields here
    street = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    bulding = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'bulding'
    }))
    flat = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'flat'
    }))
    post_code = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'city'
    }))
