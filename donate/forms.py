from django import forms
from .models import Donate


class BarcodeForm(forms.Form):
    code = forms.CharField(label='CODE', max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Verification Code..'}))


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
