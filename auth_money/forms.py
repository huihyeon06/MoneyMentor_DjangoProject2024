from django import forms
from .models import Content, Term


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['name', 'substance', 'contents_img']

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['name', 'substance']

