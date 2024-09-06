from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Назва книги', widget=forms.TextInput(attrs={'class': 'form-input'}))
    author = forms.CharField(label='Автор', widget=forms.TextInput(attrs={'class': 'form-input'}))
    published_date = forms.DateField(label='Дата публікації' ,widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    isbn = forms.IntegerField(label='Номер ISBN', widget=forms.NumberInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'class': 'form-input'}),
            'published_date': forms.DateInput(attrs={'class': 'form-input'}),
            'isbn': forms.NumberInput(attrs={'class': 'form-input'}),
        }