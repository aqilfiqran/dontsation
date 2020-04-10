from django import forms


class BarcodeForm(forms.Form):
    code = forms.CharField(label='code', max_length=100)
