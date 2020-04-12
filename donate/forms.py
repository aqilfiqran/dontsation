from django import forms
from .models import Donate


class BarcodeForm(forms.Form):
    code = forms.CharField(label='code', max_length=200)


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'email', 'donation']
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Masukkan nama anda'
        #         }
        #     ),
        #     'email': forms.EmailField(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Masukkan email anda'
        #         }
        #     ),
        #     'donation': forms.IntegerField(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Masukkan donasi anda'
        #         }
        #     )
        # }
