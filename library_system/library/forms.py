from django import forms
from .models import Book, Author, Borrower, Transaction

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publish_date']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'borrower', 'return_date']