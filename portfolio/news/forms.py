from .models import News, Group_of_news
from django import forms
from django.forms import ModelForm


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('title', 'full_text', 'img', 'author', 'author_img', 'group')

        widgets = {
            'title': forms.TextInput(attrs={'class': '123', 'placeholder': 'title'}),
            'full_text': forms.Textarea(attrs={'class': '123', 'placeholder': 'full text'}),
            'author': forms.TextInput(attrs={'class': '123', 'placeholder': 'author'}),
        }

