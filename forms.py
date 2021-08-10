from django import forms
from django.forms import fields, formsets
from library.models import Author, Book

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)

    class Meta():
        model = Book
        fields = '__all__'
        # fields = ['ISBN', 'title', 'description', 'price', 'copy_count', 'year_release', 'author']