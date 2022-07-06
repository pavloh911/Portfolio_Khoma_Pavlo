from .models import MessagesForUs
from django import forms
from django.forms import ModelForm


class MessagesForUsForm(ModelForm):
    class Meta:
        model = MessagesForUs
        fields = ('user_name', 'user_email', 'user_message')

        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'user_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'message'})
        }
