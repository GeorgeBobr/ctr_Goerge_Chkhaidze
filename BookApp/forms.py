from django import forms
from django.forms import widgets

class BookForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label="Автор")
    email = forms.EmailField(required=True)
    text = forms.CharField(required=True, label="Описание", widget=widgets.Textarea(attrs={"cols": 30, "rows": 5, "class": "test"}))