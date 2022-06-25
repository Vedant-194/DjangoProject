from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'book_image', 'author', 'book_pdf', 'genre']
