from .models import User
from django import forms


class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'no_hp', 'password']
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Password'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Name'
                }
            ),
            'no_hp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Phone Number'
                }
            ),
        }
