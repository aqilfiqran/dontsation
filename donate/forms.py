from django import forms
from .models import Donate


class BarcodeForm(forms.Form):
    code = forms.CharField(label='CODE', max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-text', 'placeholder': 'Your Verification Code..'}))


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'email', 'donation']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-text',
                    'placeholder': 'Masukkan nama anda'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-text',
                    'type': 'email',
                    'placeholder': 'Masukkan email anda'
                }
            ),
            'donation': forms.TextInput(
                attrs={
                    'type': 'number',
                    'class': 'form-text',
                    'placeholder': 'Masukkan donasi anda'
                }
            )
        }
